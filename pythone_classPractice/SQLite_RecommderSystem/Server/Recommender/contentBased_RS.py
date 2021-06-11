"""
#Content(metadata) Based Recommender
    To build our standard metadata based content recommender, 
    we will need to merge our current dataset with the crew and the keyword datasets.

    Crew: From the crew, we will only pick the director as our feature since the others don't contribute that much to the feel of the movie.
    Cast: Choosing Cast is a little more tricky. 
    Lesser known actors and minor roles do not really affect people's opinion of a movie. 
    Therefore, we must only select the major characters and their respective actors. 
    Arbitrarily we will choose the top 3 actors that appear in the credits list.
"""
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
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from ast import literal_eval
import sqlite3

from DB.DBConnection import DBConnection
from DB.DBInitializer import DBInitializer

class contentBased_RS:
    def __init__(self):
        self.conn = sqlite3.connect('./UserMovie.db')  #連接資料庫
        
        self.smd = pd.read_sql("SELECT * FROM MovieData_Table;", self.conn)
        print("contentBased_RS initialized")
    
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

        #CountVectorizer 結合 TfidfTransformer
        count_vectorizer = CountVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
        count_vectorizer_matrix = count_vectorizer.fit_transform(self.smd['soup'])

        Tfidftransformer  = TfidfTransformer()
        tfidf_matrix2 = Tfidftransformer.fit_transform(count_vectorizer_matrix)
        self.cosine_sim2 = cosine_similarity(tfidf_matrix2, tfidf_matrix2)

        recommendMovie = self.contentBased_recommendations(Watched_Movie_title, Recommed_Top_Num)
        #print("\nBecause you watch :{}, \nso we recommend you the top-{} most similar movies(Content Based RS Considering Popularity and Ratings):\n{}".format(self.Watched_Movied_title, self.Recommed_Top_Num, recommendMovie))

        recommendMovie['indices'] = recommendMovie.index
        recommendMovie.reset_index(drop=True, inplace=True)
        #dict_recommendMovie = recommendMovie.to_dict('index')
        list_of_dicts_recommendMovie = list(recommendMovie.T.to_dict().values())
        #print(list_of_dicts_recommendMovie)
        return list_of_dicts_recommendMovie
    
    def get_director(self, x):
        for i in x:
            if i['job'] == 'Director':
                return i['name']
        return np.nan

    def weighted_rating(self, x):
        #Calculate score using the IMDB formula of weighted rating (WR)
        vote_counts = self.smd[self.smd['vote_count'].notnull()]['vote_count'].astype('int')
        vote_averages = self.smd[self.smd['vote_average'].notnull()]['vote_average'].astype('int')
        self.C = vote_averages.mean()
        self.m = vote_counts.quantile(0.8)

        v = x['vote_count']
        R = x['vote_average']
        return (v/(v+self.m) * R) + (self.m/(self.m+v) * self.C)

    def contentBased_recommendations(self, title, Recommed_Top_Num = 10):
        # improved_recommendations
        # Considering Popularity and Ratings
        idx = self.indices[title]
        sim_scores = list(enumerate(self.cosine_sim2[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:50]
        movie_indices = [i[0] for i in sim_scores]
        
        movies = self.smd.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'year', 'id', 'genres']]
        vote_counts = movies[movies['vote_count'].notnull()]['vote_count'].astype('int')
        vote_averages = movies[movies['vote_average'].notnull()]['vote_average'].astype('int')
        C = vote_averages.mean()
        m = vote_counts.quantile(0.60)
        qualified = movies[(movies['vote_count'] >= m) & (movies['vote_count'].notnull()) & (movies['vote_average'].notnull())]
        qualified['vote_count'] = qualified['vote_count'].astype('int')
        qualified['vote_average'] = qualified['vote_average'].astype('int')
        qualified['wr'] = qualified.apply(self.weighted_rating, axis=1)
        qualified = qualified.sort_values('wr', ascending=False).head(Recommed_Top_Num)
        return qualified

    
