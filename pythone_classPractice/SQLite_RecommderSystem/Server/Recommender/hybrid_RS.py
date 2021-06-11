import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from ast import literal_eval

from surprise import Reader, Dataset, SVD #pip install scikit-surprise  之前必須先下載"pip install wheel"、"Microsoft Visual C++ 14.0 or greater"
from surprise.model_selection import cross_validate, train_test_split

from DB.DBConnection import DBConnection
from DB.DBInitializer import DBInitializer

import sqlite3

class hybrid_RS:
    def __init__(self):
        self.conn = sqlite3.connect('./UserMovie.db')  #連接資料庫
        
        self.smd = pd.read_sql("SELECT * FROM MovieData_Table;", self.conn)
        self.ratings = pd.read_sql("SELECT * FROM Ratings_Table;", self.conn)
        self.id_map = pd.read_sql("SELECT * FROM MovieID_map_Table;", self.conn)
        self.id_map.set_index('id', inplace=True)
        print("hybrid_RS initialized")

    def execute(self, userId, Watched_Movie_title, Watched_Movie_ID, Recommed_Top_Num):

        self.titles = self.smd['title']
        self.indices = pd.Series(self.smd.index, index=self.smd['title'])
        
        #原本cast crew keywords原本為json形式的字符串，我們用literal_eval，將字符串型的list,tuple,dict轉變成原有的類型
        self.smd['genres'] = self.smd['genres'].fillna('').apply(literal_eval)
        self.smd['cast'] = self.smd['cast'].apply(literal_eval)
        self.smd['crew'] = self.smd['crew'].apply(literal_eval)
        self.smd['keywords'] = self.smd['keywords'].apply(literal_eval)
        self.smd['cast_size'] = self.smd['cast'].apply(lambda x: len(x))
        self.smd['crew_size'] = self.smd['crew'].apply(lambda x: len(x))

        self.smd['cast'] = self.smd['cast'].apply(lambda x: x[:3] if len(x) >=3 else x) #choose the top 3 actors

        self.smd['director'] = self.smd['crew'].apply(self.get_director)
        self.smd['director'] = self.smd['director'].astype('str').apply(lambda x: str.lower(x.replace(" ", "")))
        self.smd['director'] = self.smd['director'].apply(lambda x: [x,x, x])

        self.smd['soup'] = self.smd['keywords'] + self.smd['cast'] + self.smd['director'] + self.smd['genres']
        self.smd['soup'] = self.smd['soup'].apply(lambda x: ' '.join(x))

        self.smd = self.smd.reset_index()

        self.titles = self.smd['title']
        self.indices = pd.Series(self.smd.index, index=self.smd['title'])
        #============================= Hybrid Recommender ===============================
        #CountVectorizer 結合 TfidfTransformer
        count_vectorizer = CountVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
        count_vectorizer_matrix = count_vectorizer.fit_transform(self.smd['soup'])

        Tfidftransformer  = TfidfTransformer()
        tfidf_matrix2 = Tfidftransformer.fit_transform(count_vectorizer_matrix)
        self.cosine_sim2 = cosine_similarity(tfidf_matrix2, tfidf_matrix2)


        reader = Reader()
        data = Dataset.load_from_df(self.ratings[['userId', 'movieId', 'rating']], reader)

        self.svd = SVD(n_factors=100)
        trainset, testset = train_test_split(data, test_size=.5)
        self.svd.fit(trainset)
        
        recommendMovie_hybrid = self.hybrid_recommendations(userId, Watched_Movie_title, Recommed_Top_Num)
        #print("\nBecause you watch :{}, \nso we recommend you the top-{} most similar movies(Hybrid):\n{}".format(self.Watched_Movie_title, self.Recommed_Top_Num, recommendMovie_hybrid))

        recommendMovie_hybrid['indices'] = recommendMovie_hybrid.index
        recommendMovie_hybrid.reset_index(drop=True, inplace=True)
        #dict_recommendMovie_hybrid = recommendMovie_hybrid.to_dict('index')
        list_of_dicts_recommendMovie_hybrid = list(recommendMovie_hybrid.T.to_dict().values())
        #print(list_of_dicts_recommendMovie_hybrid)
        return list_of_dicts_recommendMovie_hybrid

    def hybrid_recommendations(self, userId, title, Recommed_Top_Num = 10):
        idx = self.indices[title]
        #tmdbId = id_map.loc[title]['id']
        #print(idx)
        #movie_id = id_map.loc[title]['movieId']
        
        sim_scores = list(enumerate(self.cosine_sim2[int(idx)]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:Recommed_Top_Num+1]   #從1開始而不是從0，因為第0的sim_scores值是1(自己)

        movie_indices = [i[0] for i in sim_scores]
        
        movies = self.smd.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'year', 'id', 'genres']]
        #算出SVD的est(Estimate_Scores)
        movies['est'] = movies['id'].apply(lambda x: self.svd.predict(userId, self.id_map.loc[x]['movieId']).est)
        #推薦上我們保留Top-2是Content based RS出來的結果
        movies_contentbased = movies[0:2]
        #推薦上是我們content based RS的Top-3~end,並根據collaborative filtering RS 做分數(Estimate_Scores)排序
        movies = movies[2:Recommed_Top_Num+1].sort_values('est', ascending=False)

        movies = pd.concat([movies_contentbased, movies])
        return movies
    def get_director(self, x):
        for i in x:
            if i['job'] == 'Director':
                return i['name']
        return np.nan



