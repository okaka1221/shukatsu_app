from rest_framework.views import exception_handler

from janome.tokenizer import Tokenizer
from collections import defaultdict
import re

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
    
    return response

# extract nouns from text given
def counter(text):
    tokenizer = Tokenizer()
    texts = text.splitlines()
    words = []
    word_count = defaultdict(int)

    for text in texts:
        tokens = tokenizer.tokenize(text)
        for token in tokens:
            # extract nouns
            pos = token.part_of_speech.split(',')[0]
            if pos in ['名詞']:
                base = token.base_form
                if base not in ["こと", "よう", "そう", "これ", "それ", "もの", "ため"]:
                    # remove numbers
                    if len(re.findall(r'([+-]?[0-9]+\.?[0-9]*)', base)) == 0:
                        words.append(base)
                        word_count[base] += 1
    
    return words, word_count