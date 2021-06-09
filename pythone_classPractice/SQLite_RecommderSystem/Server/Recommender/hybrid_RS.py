"""
參考網站:
1.Hybrid RS
https://www.kaggle.com/rounakbanik/movie-recommender-systems?select=credits.csv
2.Kaggle Dataset - The Movies Dataset
https://www.kaggle.com/rounakbanik/the-movies-dataset
3.SQLite DB to pandas
https://www.learncodewithmike.com/2021/05/pandas-and-sqlite.html
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from surprise import Reader, Dataset, SVD #pip install scikit-surprise  之前必須先下載"pip install wheel"、"Microsoft Visual C++ 14.0 or greater"
from surprise.model_selection import cross_validate, train_test_split

import warnings; warnings.simplefilter('ignore')

import pandas as pd
import sqlite3
 
conn = sqlite3.connect('../UserMovie.db')  #建立資料庫
smd = pd.read_sql("SELECT * FROM MovieData_Table", conn)

titles = smd['title']
indices = pd.Series(smd.index, index=smd['title'])

smd['tagline'] = smd['tagline'].fillna('')
smd['description'] = smd['overview'] + smd['tagline']
smd['description'] = smd['description'].fillna('')

tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(smd['description'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def get_recommendations(title, Recommed_Top_Num=10):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:Recommed_Top_Num+1]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]


WatchedMovie = "Toy Story"
Recommed_Top_Num = 20
recommendMovie = get_recommendations(WatchedMovie, Recommed_Top_Num)
print("\nBecause you watch :{}, \nso we recommend you the top-{} most similar movies(Content Based):\n{}".format(WatchedMovie, Recommed_Top_Num, recommendMovie))