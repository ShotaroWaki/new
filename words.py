from gensim.models import Word2Vec
import pandas as pd
import numpy as np
from gensim.models import KeyedVectors
import scipy.spatial.distance
from model import calculate_language_vector


def search_most_similar(emotion_vector):
    df = pd.read_csv('word_model.csv')
    max_lang = df.iloc[0,0]
    tmp_max =0
    min_lang = df.iloc[0,0]
    tmp_min =1

    for i in range(len(df)):
        vect = calculate_language_vector(df.iloc[i,1])
        score = 1-scipy.spatial.distance.cosine(emotion_vector, vect)
        if score > tmp_max:
            max_lang = df.iloc[i,0]
            tmp_max = score
        if score < tmp_min:
            min_lang = df.iloc[i,0]
            tmp_min = score

    return max_lang, min_lang

data = pd.read_csv('word_model.csv')
emotion_vector = calculate_language_vector(data)

dictionary = pd.DataFrame('./model.vec')
print(dictionary.head())

