from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('ecommerce_vectors.txt', binary=False) 

def findKeywords(likedKeywords, dislikedKeywords):
    result = model.most_similar(positive=likedKeywords, negative=dislikedKeywords, topn=2)
    return result