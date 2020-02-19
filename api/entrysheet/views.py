from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from .serializers import EntrySheetSerializer

from api.entrysheet.wordcloud import WordCloudGenerator
from api.entrysheet.similarity_score import SimilarityScore
from api.entrysheet.classification import Classifier
from api.entrysheet.utils import counter

import logging
logging.disable(logging.WARNING)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
graph = tf.get_default_graph()

wordcloud = WordCloudGenerator()
sim_score = SimilarityScore()
classifier = Classifier()

class EntrySheetResult(APIView):
    def post(self, request, format=None):
        data = JSONParser().parse(request)

        keywords = data['keywords'].replace('\u3000', ' ')
        text = data['text'].replace('\u3000', ' ')

        words, word_counts = counter(text)

        if len(words) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        # check validation and save data in db
        serializer = EntrySheetSerializer(data={'text': data['text'], 'label': data['label']})
        if serializer.is_valid() and len(text) > 150:
            serializer.save()

        keywords, keyword_counts = counter(keywords)

        wordcloud_obj = wordcloud.generate(words)
        encoded_wordcloud = wordcloud.to_encoded_image(wordcloud_obj)

        keyword_sim_score = None
        if len(keywords) > 0:
            keyword_sim_score = sim_score.calc_score(word_counts, keywords)
        
        global graph
        with graph.as_default():
            jikoPR_score = classifier.predict(data['text']) * 100

        res = {
            'encoded_wordcloud': encoded_wordcloud,
            'keyword_sim_score': keyword_sim_score,
            'jikoPR_score':  jikoPR_score,
        }

        return Response(res)