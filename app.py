from flask import Flask, abort, request, render_template
from model.model import find_keywords
from flask_cors import CORS
import json

app =  Flask(__name__)
cors = CORS(app)

@app.route("/")
def home():
    return {"Endpoints": {"/model": "accepts POST request containing keywords which returns related keywords"}}

@app.route("/model", methods=['POST'])
def model():
    try:
        words = request.json
        return json.dumps({'keywords': find_keywords(words['positive'], words['negative'] )})
    except:
        abort(400)

@app.route("/*")
def not_found():
    abort(404)

@app.errorhandler(400)
def handle_400(e):
    return render_template("400.html"), 400