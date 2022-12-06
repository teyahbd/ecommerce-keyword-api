from gensim.models import KeyedVectors
import os

data_path = os.path.dirname(os.path.abspath(__file__)) + "/ecommerce_vecs.txt"

model = KeyedVectors.load_word2vec_format(data_path, binary=False) 

def find_keywords(liked_keywords, disliked_keywords):
    result = model.most_similar(positive=liked_keywords, negative=disliked_keywords, topn=2)
    return result
