from django.contrib.staticfiles.storage import staticfiles_storage

import logging
logging.disable(logging.WARNING)
from gensim.models import KeyedVectors

class SimilarityScore():
    """
    Calculate similarity score between text and keywords
    """
    def __init__(self):
        self.model_path = staticfiles_storage.path('text_analysis/wikipedia_entity_model')
        self.model = KeyedVectors.load(self.model_path)

    def calc_score(self, word_counts, keywords):
        word_counts = sorted(word_counts.items(), key=lambda x:x[1], reverse=True)
        max_freq = word_counts[0][1]

        num_keywords = len(keywords)
        num_keywords_found = 0
        total_score = 0

        for keyword in keywords:
            max_score = 0

            if keyword in self.model.wv.vocab:
                num_keywords_found += 1
                
                for word_count in word_counts:
                    try:
                        similarity = self.model.wv.similarity(keyword, word_count[0])
                        score = similarity * word_count[1] / max_freq
                        
                        if score > max_score:
                            max_score = score
                    
                    except KeyError:
                        pass
                
            total_score += max_score

        return total_score / num_keywords_found * 100 if num_keywords_found > 0 else None