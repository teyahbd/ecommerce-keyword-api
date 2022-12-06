from gensim.models import Word2Vec 

# Create and train the model using the text corpus

model = Word2Vec(min_count=1, corpus_file="./cleaned_dataset.txt")

# Extract the word vectors from the model

word_vectors = model.wv

# Save the word vectors as a text file which can be loaded at a later date

word_vectors.save_word2vec_format('ecommerce_vecs.txt', binary= False)