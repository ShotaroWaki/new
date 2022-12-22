from flask import Flask, render_template, request
from gensim.models import Word2Vec
import pandas as pd
import numpy as np
from gensim.models import KeyedVectors
import scipy.spatial.distance
from model import calculate_emotion_vector,search_most_similar

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search")
def about():
    return render_template('search.html')

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/show',methods=['GET',"POST"])
def result():
    if request.method == 'GET':
        return render_template('show.html')
    elif request.method == 'POST':
        char = request.form.getlist("character")
        ideal = request.form.getlist("ideal")
        feeling = request.form.getlist("feeling")
        keyword = request.form.getlist("keyword")
        key_list = char + ideal + feeling + keyword
        emothion_vector = calculate_emotion_vector(key_list)
        max_lang, min_lang = search_most_similar(emothion_vector)
        return render_template("show.html",max_lang = max_lang, min_lang = min_lang)

if __name__ == "__main__":
    app.run(debug=True)