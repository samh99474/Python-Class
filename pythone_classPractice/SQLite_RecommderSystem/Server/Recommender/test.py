"""
參考網站:
1.Hybrid RS
https://www.kaggle.com/rounakbanik/movie-recommender-systems?select=credits.csv
2.Kaggle Dataset - The Movies Dataset
https://www.kaggle.com/rounakbanik/the-movies-dataset
3.SQLite DB to pandas
https://www.learncodewithmike.com/2021/05/pandas-and-sqlite.html
4.文本數據預處理 - 詞頻、資訊檢索與文本挖掘 (TF-IDF、CountVectorizer)
https://zh.codeprj.com/blog/8f9c1e1.html
5. dataframe to dict
https://kanoki.org/2020/03/24/convert-pandas-dataframe-to-dictionary/
https://www.programiz.com/python-programming/nested-dictionary
6. dataframe to list-of-dictionaries
https://stackoverflow.com/questions/29815129/pandas-dataframe-to-list-of-dictionaries
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
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
ratings = pd.read_sql("SELECT * FROM Ratings_Table", conn)
id_map = pd.read_sql("SELECT * FROM MovieID_map_Table", conn)
id_map.set_index('id', inplace=True)

titles = smd['title']
indices = pd.Series(smd.index, index=smd['title'])

"""#Content(metadata) Based Recommender
To build our standard metadata based content recommender, 
we will need to merge our current dataset with the crew and the keyword datasets.
Crew: From the crew, we will only pick the director as our feature since the others don't contribute that much to the feel of the movie.
Cast: Choosing Cast is a little more tricky. 
Lesser known actors and minor roles do not really affect people's opinion of a movie. 
Therefore, we must only select the major characters and their respective actors. 
Arbitrarily we will choose the top 3 actors that appear in the credits list.
"""
#原本cast crew keywords原本為json形式的字符串，我們用literal_eval，將字符串型的list,tuple,dict轉變成原有的類型
smd['genres'] = smd['genres'].fillna('').apply(literal_eval)
smd['cast'] = smd['cast'].apply(literal_eval)
smd['crew'] = smd['crew'].apply(literal_eval)
smd['keywords'] = smd['keywords'].apply(literal_eval)
smd['cast_size'] = smd['cast'].apply(lambda x: len(x))
smd['crew_size'] = smd['crew'].apply(lambda x: len(x))

smd['cast'] = smd['cast'].apply(lambda x: x[:3] if len(x) >=3 else x) #choose the top 3 actors

def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return np.nan
smd['director'] = smd['crew'].apply(get_director)
smd['director'] = smd['director'].astype('str').apply(lambda x: str.lower(x.replace(" ", "")))
smd['director'] = smd['director'].apply(lambda x: [x,x, x])

smd['soup'] = smd['keywords'] + smd['cast'] + smd['director'] + smd['genres']
smd['soup'] = smd['soup'].apply(lambda x: ' '.join(x))

#CountVectorizer 結合 TfidfTransformer
count_vectorizer = CountVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
count_vectorizer_matrix = count_vectorizer.fit_transform(smd['soup'])

Tfidftransformer  = TfidfTransformer()
tfidf_matrix2 = Tfidftransformer.fit_transform(count_vectorizer_matrix)
cosine_sim2 = cosine_similarity(tfidf_matrix2, tfidf_matrix2)

smd = smd.reset_index()
titles = smd['title']
indices = pd.Series(smd.index, index=smd['title'])


"""
# improved_recommendations
# Considering Popularity and Ratings
Popularity and Ratings
One thing that we notice about our recommendation system is that it recommends movies regardless of ratings and popularity. 
It is true that Batman and Robin has a lot of similar characters as compared to The Dark Knight but it was a terrible movie 
that shouldn't be recommended to anyone.
Therefore, we will add a mechanism to remove bad movies and return movies which are popular and have had a good critical response.
I will take the top 25 movies based on similarity scores and calculate the vote of the 60th percentile movie. 
Then, using this as the value of  m , 
we will calculate the weighted rating of each movie using IMDB's formula like we did in the Simple Recommender section
"""
"""
Calculate score using the IMDB formula of weighted rating (WR)
v is the number of votes for the movie
m is the minimum votes required to be listed in the chart
R is the average rating of the movie
C is the mean vote across the whole report
"""
vote_counts = smd[smd['vote_count'].notnull()]['vote_count'].astype('int')
vote_averages = smd[smd['vote_average'].notnull()]['vote_average'].astype('int')
C = vote_averages.mean()
m = vote_counts.quantile(0.8)

def weighted_rating(x):
    #Calculate score using the IMDB formula of weighted rating (WR)
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m) * R) + (m/(m+v) * C)

def contentBased_recommendations(title, Recommed_Top_Num = 10):
    # improved_recommendations
    # Considering Popularity and Ratings
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim2[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:50]
    movie_indices = [i[0] for i in sim_scores]
    
    movies = smd.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'year', 'id', 'genres']]
    vote_counts = movies[movies['vote_count'].notnull()]['vote_count'].astype('int')
    vote_averages = movies[movies['vote_average'].notnull()]['vote_average'].astype('int')
    C = vote_averages.mean()
    m = vote_counts.quantile(0.60)
    qualified = movies[(movies['vote_count'] >= m) & (movies['vote_count'].notnull()) & (movies['vote_average'].notnull())]
    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['vote_average'] = qualified['vote_average'].astype('int')
    qualified['wr'] = qualified.apply(weighted_rating, axis=1)
    qualified = qualified.sort_values('wr', ascending=False).head(Recommed_Top_Num)
    return qualified

WatchedMovie = "Toy Story"
Recommed_Top_Num = 20
recommendMovie = contentBased_recommendations(WatchedMovie, Recommed_Top_Num)
print("\nBecause you watch :{}, \nso we recommend you the top-{} most similar movies(Content Based RS Considering Popularity and Ratings):\n{}".format(WatchedMovie, Recommed_Top_Num, recommendMovie))

#============================= Hybrid Recommender ===============================

reader = Reader()
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

svd = SVD(n_factors=100)
trainset, testset = train_test_split(data, test_size=.5)
svd.fit(trainset)

def convert_int(x):
    try:
        return int(x)
    except:
        return np.nan

def hybrid_recommendations(userId, title, Recommed_Top_Num = 10):
    idx = indices[title]
    #tmdbId = id_map.loc[title]['id']
    #print(idx)
    #movie_id = id_map.loc[title]['movieId']
    
    sim_scores = list(enumerate(cosine_sim2[int(idx)]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:Recommed_Top_Num+1]   #從1開始而不是從0，因為第0的sim_scores值是1(自己)

    movie_indices = [i[0] for i in sim_scores]
    
    movies = smd.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'year', 'id', 'genres']]
    #算出SVD的est(Estimate_Scores)
    movies['est'] = movies['id'].apply(lambda x: svd.predict(userId, id_map.loc[x]['movieId']).est)
    #推薦上我們保留Top-2是Content based RS出來的結果
    movies_contentbased = movies[0:2]
    #推薦上是我們content based RS的Top-3~end,並根據collaborative filtering RS 做分數(Estimate_Scores)排序
    movies = movies[2:Recommed_Top_Num+1].sort_values('est', ascending=False)

    movies = pd.concat([movies_contentbased, movies])
    return movies


User_ID = 1
WatchedMovie = "Toy Story"
Recommed_Top_Num = 20
recommendMovie_hybrid = hybrid_recommendations(User_ID, WatchedMovie, Recommed_Top_Num)
print("\nBecause you watch :{}, \nso we recommend you the top-{} most similar movies(Hybrid):\n{}".format(WatchedMovie, Recommed_Top_Num, recommendMovie_hybrid))

recommendMovie['indices'] = recommendMovie.index
recommendMovie_hybrid['indices'] = recommendMovie_hybrid.index

recommendMovie.reset_index(drop=True, inplace=True)
recommendMovie_hybrid.reset_index(drop=True, inplace=True)

"""dict_recommendMovie = recommendMovie.to_dict('index')
dict_recommendMovie_hybrid = recommendMovie_hybrid.to_dict('index')"""

list_of_dicts_recommendMovie = list(recommendMovie.T.to_dict().values())
list_of_dicts_recommendMovie_hybrid = list(recommendMovie_hybrid.T.to_dict().values())
print(list_of_dicts_recommendMovie_hybrid)