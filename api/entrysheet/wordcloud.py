from django.contrib.staticfiles.storage import staticfiles_storage

import logging
logging.disable(logging.WARNING)
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import base64
import io

class WordCloudGenerator():
    """
    Generate wordcloud
    """
    def __init__(self):
        self.stop_word_path = staticfiles_storage.path('text_analysis/stop_words.txt')
        self.font_path = staticfiles_storage.path('text_analysis/VL-Gothic-Regular.ttf')

    def generate(self, words):
        words_joined = ' '.join(words)

        stop_words = set(map(str.strip, open(self.stop_word_path).readlines()))

        wordcloud = WordCloud(
            background_color="white", 
            relative_scaling=1, 
            max_words=100, 
            font_path=self.font_path, 
            width=600, height=600, 
            stopwords=set(stop_words)
        ).generate(words_joined)

        return wordcloud

    def to_encoded_image(self, wordcloud):
        img = wordcloud.to_image()
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        encoded_img = base64.b64encode(buffer.getvalue())

        return encoded_img