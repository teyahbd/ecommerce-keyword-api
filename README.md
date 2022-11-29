# Machine Learning Model

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

``` npm run setup ```

To generate the dataset that will be used for the Python model.

Then run:

``` npm run start```

To start the server and enable it to go live. It runs on port 8000.