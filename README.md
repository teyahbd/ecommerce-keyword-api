# Word2Vec Keyword Recommendation API

<div align="center">
  <a href="https://northcoders.com/projects/nov-2022/santas-little-helper">
    <img src="images/logo.png" alt="Santa's Little Helper Logo">
  </a>

  <p align="center">
    An app that uses machine learning to help you with your Christmas shopping!
    <br>
    <a href="https://github.com/robcarter123/react-final-project">Main App Repo</a>
    ·
    <a href="https://northcoders.com/projects/nov-2022/santas-little-helper">Demo</a>
    ·
    <a href="https://github.com/2202Hannah/final-project-be-ebay">eBay API Repo</a>
  </p>

  <details>
  <summary>Table of Contents</summary>
  <div>
    <a href="#about-this-repo">About This Repo</a><br>
    <a href="#built-with">Built With</a><br>
    <a href="#getting-started">Getting Started</a><br>
    <a href="#getting-started">API Usage</a><br>
    <a href="#testing">Testing</a><br>
    <a href="#credits">Credits</a><br>
  </div>
</details>
</div>

# About This Repo

This API forms part of a group project completed on the Northcoders software development bootcamp. Santa's Little Helper is an app created in React Native which uses a Word2Vec machine learning model to help users find an ideal present. Please find the main app repo here for further details and our project page with an app demo can be found here.

Link to currently hosted page

wuickly explain project flow here

This is a small server that contains within it a python script to output semantically similar words when given one or more words as input. The post request accepts inputs in the following way:
{ [ postive ], [ negative ] } where both positive and negative should be arrays of strings.

Word2vec is a technique for natural language processing published in 2013. The word2vec algorithm uses a neural network model to learn word associations from a large corpus of text. Once trained, such a model can detect synonymous words or suggest additional words for a partial sentence. We used the suggested similar words to feedback keywords relating to gifts to the frontend of our project.

There are two uses for this repo:

1. Creating a Flask REST API which uses machine learning and NLP to recommend related keywords
2. Training custom word vectors with Word2Vec using an eCommerce dataset (see the folder `/model_training`)

For our app, we trained these custom word vectors first to then use in the model of our API. We've included the files for training word vectors in this repo for convenience however, this process is separate to creating the API. See the "Getting Started" section for more details on using each part of this repo.

<p align="right">(<a href="#word2vec-keyword-api">back to top</a>)</p>

# Built With

We have used Python to both train our word vectors and create this API. Key technologies we've used in development are:

- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [pandas](https://pandas.pydata.org/)
- [GENSIM](https://pypi.org/project/gensim/)
- [Word2Vec](https://code.google.com/archive/p/word2vec/)
- [pytest](https://docs.pytest.org/en/7.2.x/)
- [Jupyter Notebook](https://jupyter.org/)

Details on development of the React Native app can be found in the [main app repo](https://github.com/robcarter123/react-final-project).

<p align="right">(<a href="#word2vec-keyword-api">back to top</a>)</p>

# Getting Started

As mentioned, there are two uses for this repo - running an API and training a custom set of word vectors. If you only wish to set up the API, follow the installation instructions below. For details on our word vector training process, see this <a href="#training-custom-word-vectors-using-word2vec">later section</a>. However, it is not necessary to train the word vectors to run the API as our pre-trained vectors are included in this repo (`/model/ecommerce_vecs.txt`).

## Installation

You can get started using a local version of our API by following these steps:

### 1. Clone this repo

You can clone this repo locally using the command:

```
git clone https://github.com/teyahbd/ecommerce-keyword-api.git
```

### 2. Set up a virtual environment

Before installing the required packages, it is convention in Python to create a local virtual environment to install these packages within. To do this, navigate into the main directory of this project and run:

```
python3 -m venv venv
```

To enter the virtual environment, both now and at later points, you can use the command:

```
source venv/bin/activate
```

The name of the virtual environment (venv) should appear on your command line to indicate you are currently working within the virtual environment. In order to have access to the packages we will install in the next step, it's important to check you are within the environment when working with this repo.

### 3. Install required packages

After ensuring you are within the virtual environment, use the `requirements.txt` file to install the requirements for this project via `pip` with the command:

```
pip install -r requirements.txt
```

### 4. Launch Flask app locally

To run the Flask app on your local server, you can use the command:

```
flask run
```

Note: Flask will default to using port 5000.

<p align="right">(<a href="#word2vec-keyword-api">back to top</a>)</p>

# API Usage

Since this API was created for our React Native app to interact with our Word2Vec model, it contains only 2 endpoints. Here is a brief overview of the intended flow of this API:

1. A user submits a list of zero or more positive words and a list of zero of more negative words to the API in a POST request.
2. These two lists are passed to our Word2Vec keyword recommendation model which uses our custom word vectors to find the "most similar" words to the positive list (and/or the "least similar" to the negative list).
3. The API responds to the POST request with a list of the two recommended words generated by the model.

Essentially, the API recommends similar words based on the submitted words. The list of positive words contribute positively to the similarity, and the list of negative words contribute negatively. In use for our app, the API takes a list of positive keywords generated from items a user has liked and a list of negative keywords generated from items the user has disliking. More details the function used for these word vector calculations can be found [here](https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.KeyedVectors.most_similar).

## GET /

Responds with a list of all the current API endpoints.

#### Example Response

```
{
  "Endpoints": {
    "/model": "accepts POST request containing keywords which returns related keywords"
  }
}
```

## POST /model

Responds with an object containing a list of the two "most similar" words to the words submitted by the user.

### Request

The request object should have exactly two keys - `positive` and `negative`. Each key should have a value of a list of strings containing words accepted by the Word2Vec model. Empty arrays are accepted however, both keys must always be present on the request object.

#### Example Request

```
{
	"positive": ["heart", "chair"],
	"negative": ["star"]
}

```

### Response

The response object will have a key of `keywords`. The list returned will contain exactly two values - the two "most similar" words to the submitted words. Each word is returned with a corresponding value which represents it's similarity to the positive words from the request object (and/or their dissimilarity to the negative words). This value ranges from -1 (not very similar) to 1 (very similar).

#### Example Response

```
{
	"keywords": [
		[
			"desk",
			0.5458441972732544
		],
		[
			"camping",
			0.46846500039100647
		]
	]
}
```

## Notes

- A list of all accepted words for our Word2Vec API can be found in `model/word_list.txt`.
- ⚠️ Warning! This API focuses on the value of training custom, context-relevant word vectors as an exploration of the technology involved. Therefore, our dataset is relatively small and there are many words that do not exist on our current word list.
  - It is recommended to check which words are accepted by our API before use. If any word on either list is not accepted, currently our API will return a 400 Bad Request error.
  - If you wish to see an example using a much larger (but less relevant) word list, see our [previous repo](https://github.com/teyahbd/wiki-keyword-api) which contains an identical API but instead uses pretrained Wikipedia word vectors from GLoVe.

<p align="right">(<a href="#word2vec-keyword-api">back to top</a>)</p>

# Testing

Our Word2Vec function, API endpoints and their respective error handling is tested using `pytest` and our test files can be found within the `__tests__` folder. To run these tests for yourself, navigate into this folder (after following the API installation procedure) and run:

`python3 -m pytest`

This command can be followed by either file name (`test_app.py` or `test_model.py`) to run the tests from each file separately.

<p align="right">(<a href="#word2vec-keyword-api">back to top</a>)</p>

# Training Custom Word Vectors using Word2Vec

We've included all of our training files for training word vectors based on an eCommerce-specific dataset in the folder `/model_training`. The two Jupyter Notebooks in particular provide a useful explanation of our process. The resulting word vectors can be found in our API in the `/model` folder and are used in `model.py`.

If you wish to try this out for yourself, there are two stages to our process:

1. Preparing and cleaning the dataset
2. Training the word vectors using Word2Vec

## Prerequisites

- Follow steps 1-3 in the <a href="#getting-started">Getting Started</a> section
  - Note: You may wish to set up a separate directory and virtual environment for training the dataset. In this case, copy the folder (`/model_training`) into the new directory alongside the `requirements.txt` file and follow the Getting Started steps from there.
- Ensure you have downloaded the UCI Online Retail dataset found [here](https://archive.ics.uci.edu/ml/machine-learning-databases/00352/) and placed the `.xlsx` file within the `/model_training` folder.

## 1. Cleaning the dataset

Follow the detailed instructions found in the jupyter notebook `/model_training/clean_data.ipynb`. We have also included a basic Python script, so you can complete the steps found in the notebook in one go using the command

```
python3 clean_data.py
```

within the `/model_training` directory.

### Notes

- Expect to wait up to a few minutes when running scripts or commands in this section due to the size of the dataset.
- Check the downloaded dataset has the same file name as used in the script (`Online_Retail.txt`).

## 2. Training the word vectors

You should have generated a file called `cleaned_dataset.txt` inside the `/model_training` folder which contains the data in an appropriate format for training. Follow the detailed instructions in the second jupyter notebook `/model_training/train_model.ipynb` to train the word vectors using this data. Again, we've included a basic Python script for this so you can complete these steps in one go using the command:

```
python3 train_model.py
```

within the `/model_training` directory.

You should have now generated your own version of our word vector file inside `/model_training` called `ecommerce_vecs.txt`.

### Notes

- While the first step of cleaning the data is specific to our dataset, the second file for training word vectors should work for any corpus formatted similarly to `cleaned_dataset.txt` (i.e. a text file containing a list of sentences to train).
- If you wish to use this file for your API, replace our default file in the `/model` folder.

# Credits

This API forms part of a short project completed during the Northcoders software development bootcamp in 2022 by My Favourite Team. Check out our project page with an app demo [here](https://northcoders.com/projects/nov-2022/santas-little-helper).

## Team Members

- Teyah Brennen-Davies ([LinkedIn](https://www.linkedin.com/in/teyah-brennen-davies/)|[Github](https://github.com/teyahbd))
- Hannah Barber ([LinkedIn](https://www.linkedin.com/in/hannah-barber-036a7a97/)|[Github](https://github.com/2202Hannah))
- Byron Esson ([LinkedIn](https://www.linkedin.com/in/byron-esson-4181121a7/)|[Github](https://github.com/byronEsson))
- David Cobb ([LinkedIn](https://www.linkedin.com/in/david-cobb-925600253/)|[Github](https://github.com/DavidCobb606))
- Niall Sexton ([LinkedIn](https://www.linkedin.com/in/niall-sexton-64a9821b3)|[Github](https://github.com/NiallSexton))
- Rob Carter ([LinkedIn](https://www.linkedin.com/in/rob-carter-906145a8/)|[Github](https://github.com/robcarter123))

## Data

To train a set of custom eCommerce word vectors, we have used an online retail dataset from the [UCI machine learning repository](https://archive.ics.uci.edu/ml/index.php) which can be downloaded [here](https://archive.ics.uci.edu/ml/machine-learning-databases/00352/).

## Resources

The following resources were particularly helpful in creating this project:

- [Building a Recommendation System using Word2Vec](https://www.analyticsvidhya.com/blog/2019/07/how-to-build-recommendation-system-word2vec-python/)
- [Deploying a Python Flask Example Application Using Heroku](https://realpython.com/flask-by-example-part-1-project-setup/)
- [Best README Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#word2vec-keyword-api">back to top</a>)</p>
