from flask import Flask, abort, request
from model import findKeywords
import json

app =  Flask(__name__)

@app.route("/")
def home():
    return {"Endpoints": {"/model": "accepts POST request containing keywords which returns related keywords"}}

@app.route("/model", methods=['POST'])
def model():
    try:
        words = request.json
        return json.dumps({'keywords': findKeywords(words['positive'], words['negative'] )})
    except:
        abort(400)

@app.route("/*")
def not_found():
    abort(404)

@app.errorhandler(400)
def handle_400(e):
    return 'Request object not formatted correctly', 400