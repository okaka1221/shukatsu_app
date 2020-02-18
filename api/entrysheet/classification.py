from django.contrib.staticfiles.storage import staticfiles_storage
from .models import EntrySheetModel

import logging
logging.disable(logging.WARNING)

from keras_bert import load_trained_model_from_checkpoint, get_custom_objects
from keras import utils, Input, Model
from keras.layers import Dense, Dropout, LSTM, Bidirectional
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.models import load_model
from keras.backend import clear_session
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import sentencepiece as spm
import pandas as pd
import numpy as np
import re
import MeCab
mecab = MeCab.Tagger("-Ochasen")

class Classifier():
    """
    Classify text as true or false
    テキストがESを通過するかの確率をregressionで出す
    """
    def __init__(self):
        self.maxlen = 512
        self.bert_dim = 768
        self.bert_config_path = staticfiles_storage.path('entrysheet/bert/bert_config.json')
        self.bert_checkpoint_path = staticfiles_storage.path('entrysheet/bert/model.ckpt-1400000')
        self.bert = load_trained_model_from_checkpoint(self.bert_config_path, self.bert_checkpoint_path, seq_len=self.maxlen, training=True, trainable=False)
        
        self.sp_path = staticfiles_storage.path('entrysheet/bert/wiki-ja.model')
        self.sp = spm.SentencePieceProcessor()
        self.sp.Load(self.sp_path)
        
        self.model_path = staticfiles_storage.path('entrysheet/bert/bert_check_point.model')
        self.model = load_model(self.model_path, custom_objects=get_custom_objects())

    def predict(self, text):
        tokens = [self._get_tokens(text)]
        tokens = [tokens, np.zeros_like(tokens)]
        predict_prob = self.model.predict(tokens)[0][1]
        return predict_prob

    def train(self, test_size, epochs, batch_size, patience):
        df = pd.DataFrame(list(ESModel.objects.all().values()))
        df['label'] = df['label'] * 1

        X = []
        for text in df['text']:
            X.append(self._get_tokens(text))

        y = df['label'].values
        y = utils.np_utils.to_categorical(y)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42, shuffle=True, stratify=y)

        X_train = [X_train, np.zeros_like(X_train)]
        X_test = [X_test, np.zeros_like(X_test)]

        inputs = self.bert.inputs[:2]
        bert_output = self.bert.get_layer('Encoder-12-FeedForward-Norm').output
        x1 = Bidirectional(LSTM(256))(bert_output)
        outputs = Dropout(0.2)(x1)
        outputs = Dense(units=64)(outputs)
        outputs = Dense(units=2, activation='softmax')(outputs)

        model = Model(inputs, outputs)
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc', 'mse'])

        history = model.fit(
            X_train, y_train,
            validation_data=(X_test, y_test),
            epochs=epochs,
            batch_size=batch_size,
            shuffle=True,
            verbose=1,
            callbacks=[
                EarlyStopping(patience=patience, monitor='val_acc', mode='max'),
                ModelCheckpoint(monitor='val_acc', mode='max', filepath=self.model_path, save_best_only=True)
            ])

    def _get_tokens(self, text):
        indices = np.zeros(self.maxlen, dtype=np.float32)

        tokens = []
        tokens.append('[CLS]')
        tokens.extend(self.sp.encode_as_pieces(text))
        tokens.append('[SEP]')

        for t, token in enumerate(tokens):
            try:
                indices[t] = self.sp.piece_to_id(token)
            except:
                logging.warn(f'{token} is unknown.')
                indices[t] = self.sp.piece_to_id('<unk>')

        return indices

    
