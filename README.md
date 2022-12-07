# Machine Learning Model

the word_list.txt in the model folder gives a list of accepted keywords with the total number of words at the start.

The data used in training the model can be found here.

link to other readme and files

## About

This is part of a group project completed on the Northcoders developer bootcamp. It forms part of an App called Santa's Little Helper which uses the machine learning model to help the user with their Christmas shopping.

This is a small server that contains within it a python script to output semantically similar words when given one or more words as input. The post request accepts inputs in the following way:
{ [ postive ], [ negative ] } where both positive and negative should be arrays of strings.

Word2vec is a technique for natural language processing published in 2013. The word2vec algorithm uses a neural network model to learn word associations from a large corpus of text. Once trained, such a model can detect synonymous words or suggest additional words for a partial sentence. We used the suggested similar words to feedback keywords relating to gifts to the frontend of our project.

Link to backend repository: https://github.com/2202Hannah/final-project-be-ebay
Link to frontend repository: https://github.com/robcarter123/react-final-project

## How to run

-- download data set.

First, run

`npm run setup`

To generate the dataset that will be used for the Python model.

Then run:

` npm run start`

To start the server and enable it to go live. It runs on port 8000.

⚠️ An important note! While our dataset seems large at first glance, in the context of machine learning models it is very small - for context the wikipedia version found here () has x word vectors compared to our y. Therefore, we are sacrificing scale for relevancy. And so many words may not exist in the word corpus, which will return errors like below. This should be considered in any application of this model e.g. error handling in a keyword API.

Word2Vec uses a neural network model to learn word associations from a large corpus of text and creates word vectors which capture the semantic similarity between words.

we could've use other ones...

our goal is to create wordvectors ie numerical values

explain downstides of small dataset!

This folder has been added to this repo for convience, but likely would make sense to do this training in a separate folder and virtual environment to the api - definitely shouldn't be hosted!
For further detail on how the data was cleaned and trained, please see the jupyter notebook.

Training word vectors

We have also included basic python files for each step.

You can clean the dataset (would have to be adjusted for another dataset) using
`python3 data_cleaning.py`

discuss why ecommerce vectors

https://code.google.com/archive/p/word2vec/

credit that other tutorial

to train the model and generate the custom word vectors run this:

A list of all keywords accepted by our model can be found in the text file.

Don't host the version with the training in, see the hosting branch

the train model python file can be used with data in the correct format.

# Training Custom Word Vectors Using An Ecommerce Dataset - Part One

This notebook will detail the steps used to train our own custom Word2Vec model using ecommerce specific keywords for our Santa's Little Helper project. Initially a pre-trained dataset from Gensim (see this repo) was used, however, we later trained our own dataset for use in our specific context.

The data used was the online retail something (found here), in future an even larger dataset would be better.

There are two main stages to the process of training our word vectors (check this):

1. Cleaning the Data
2. Creating and training the word vectors

Find the second step in training.ipynb, or instead run the python file
