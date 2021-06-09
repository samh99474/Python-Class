"""
參考網站:
1.Hybrid RS
https://www.kaggle.com/rounakbanik/movie-recommender-systems?select=credits.csv
2.Kaggle Dataset - The Movies Dataset
https://www.kaggle.com/rounakbanik/the-movies-dataset
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

md = pd. read_csv('./input/movies_metadata.csv')
md['genres'] = md['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
md.head()
md['year'] = pd.to_datetime(md['release_date'], errors='coerce').apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)

#============================= Content Based===============================
links_small = pd.read_csv('./input/links_small.csv')
links_small = links_small[links_small['tmdbId'].notnull()]['tmdbId'].astype('int')
md = md.drop([19730, 29503, 35587])
md['id'] = md['id'].astype('int')
smd = md[md['id'].isin(links_small)]

smd['tagline'] = smd['tagline'].fillna('')
smd['description'] = smd['overview'] + smd['tagline']
smd['description'] = smd['description'].fillna('')

tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(smd['description'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

smd = smd.reset_index()
titles = smd['title']
indices = pd.Series(smd.index, index=smd['title'])

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

"""#Metadata Based Recommender
To build our standard metadata based content recommender, 
we will need to merge our current dataset with the crew and the keyword datasets.

Crew: From the crew, we will only pick the director as our feature since the others don't contribute that much to the feel of the movie.
Cast: Choosing Cast is a little more tricky. 
Lesser known actors and minor roles do not really affect people's opinion of a movie. 
Therefore, we must only select the major characters and their respective actors. 
Arbitrarily we will choose the top 3 actors that appear in the credits list.
"""
credits = pd.read_csv('./input/credits.csv')
keywords = pd.read_csv('./input/keywords.csv')

keywords['id'] = keywords['id'].astype('int')
credits['id'] = credits['id'].astype('int')
md['id'] = md['id'].astype('int')

md = md.merge(credits, on='id')
md = md.merge(keywords, on='id')
smd = md[md['id'].isin(links_small)]

#原本cast crew keywords原本為json形式的字符串，我們用literal_eval，將字符串型的list,tuple,dict轉變成原有的類型
smd['cast'] = smd['cast'].apply(literal_eval)
smd['crew'] = smd['crew'].apply(literal_eval)
smd['keywords'] = smd['keywords'].apply(literal_eval)
smd['cast_size'] = smd['cast'].apply(lambda x: len(x))
smd['crew_size'] = smd['crew'].apply(lambda x: len(x))

def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return np.nan
smd['director'] = smd['crew'].apply(get_director)

smd['cast'] = smd['cast'].apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else []) #smd['cast']是dict inside list型態
smd['cast'] = smd['cast'].apply(lambda x: x[:3] if len(x) >=3 else x) #choose the top 3 actors
smd['keywords'] = smd['keywords'].apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

smd['cast'] = smd['cast'].apply(lambda x: [str.lower(i.replace(" ", "")) for i in x])
smd['director'] = smd['director'].astype('str').apply(lambda x: str.lower(x.replace(" ", "")))
smd['director'] = smd['director'].apply(lambda x: [x,x, x])

s = smd.apply(lambda x: pd.Series(x['keywords']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'keyword'
s = s.value_counts()
s[:5]
s = s[s > 1]

#詞幹提取（stemming）,such as Dogs and Dog are considered the same, so we call it dog
stemmer = SnowballStemmer('english')
stemmer.stem('dogs')

def filter_keywords(x):
    words = []
    for i in x:
        if i in s:
            words.append(i)
    return words
smd['keywords'] = smd['keywords'].apply(filter_keywords)
smd['keywords'] = smd['keywords'].apply(lambda x: [stemmer.stem(i) for i in x])
smd['keywords'] = smd['keywords'].apply(lambda x: [str.lower(i.replace(" ", "")) for i in x])

smd['soup'] = smd['keywords'] + smd['cast'] + smd['director'] + smd['genres']
smd['soup'] = smd['soup'].apply(lambda x: ' '.join(x))

count = CountVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
count_matrix = count.fit_transform(smd['soup'])

cosine_sim = cosine_similarity(count_matrix, count_matrix)

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
v is the number of votes for the movie
m is the minimum votes required to be listed in the chart
R is the average rating of the movie
C is the mean vote across the whole report
"""
vote_counts = md[md['vote_count'].notnull()]['vote_count'].astype('int')
vote_averages = md[md['vote_average'].notnull()]['vote_average'].astype('int')
C = vote_averages.mean()
m = vote_counts.quantile(0.95)

def weighted_rating(x):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m) * R) + (m/(m+v) * C)

def improved_recommendations(title, Recommed_Top_Num = 10):
    # improved_recommendations
    # Considering Popularity and Ratings
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:Recommed_Top_Num+1]
    movie_indices = [i[0] for i in sim_scores]
    
    movies = smd.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'year']]
    vote_counts = movies[movies['vote_count'].notnull()]['vote_count'].astype('int')
    vote_averages = movies[movies['vote_average'].notnull()]['vote_average'].astype('int')
    C = vote_averages.mean()
    m = vote_counts.quantile(0.60)
    qualified = movies[(movies['vote_count'] >= m) & (movies['vote_count'].notnull()) & (movies['vote_average'].notnull())]
    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['vote_average'] = qualified['vote_average'].astype('int')
    qualified['wr'] = qualified.apply(weighted_rating, axis=1)
    qualified = qualified.sort_values('wr', ascending=False).head(10)
    return qualified

WatchedMovie = "Toy Story"
Recommed_Top_Num = 20
recommendMovie = get_recommendations(WatchedMovie, Recommed_Top_Num)
print("\nBecause you watch :{}, \nso we recommend you the top-{} most similar movies(Metadata Considering Popularity and Ratings):\n{}".format(WatchedMovie, Recommed_Top_Num, recommendMovie))


#============================= Collaborative Filtering ===============================

reader = Reader()
ratings = pd.read_csv('./input/ratings_small.csv')
ratings.head()

data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
#data.split(n_folds=5)

#============================= Hybrid Recommender ===============================
svd = SVD(n_factors=100)
trainset, testset = train_test_split(data, test_size=.5)
svd.fit(trainset)

def convert_int(x):
    try:
        return int(x)
    except:
        return np.nan

id_map = pd.read_csv('./input/links_small.csv')[['movieId', 'tmdbId']]
id_map['tmdbId'] = id_map['tmdbId'].apply(convert_int)
id_map.columns = ['movieId', 'id']
id_map = id_map.merge(smd[['title', 'id']], on='id').set_index('id')
#id_map = id_map.set_index('tmdbId')

def hybrid(userId, title, Recommed_Top_Num = 10):
    idx = indices[title]
    #tmdbId = id_map.loc[title]['id']
    #print(idx)
    #movie_id = id_map.loc[title]['movieId']
    
    sim_scores = list(enumerate(cosine_sim[int(idx)]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:Recommed_Top_Num+1]

    movie_indices = [i[0] for i in sim_scores]
    
    movies = smd.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'year', 'id']]
    movies['est'] = movies['id'].apply(lambda x: svd.predict(userId, id_map.loc[x]['movieId']).est)
    movies = movies.sort_values('est', ascending=False)
    return movies


User_ID = 1
WatchedMovie = "Toy Story"
Recommed_Top_Num = 20
recommendMovie_hybrid = hybrid(User_ID, WatchedMovie, Recommed_Top_Num)
print("\nBecause you watch :{}, \nso we recommend you the top-{} most similar movies(Hybrid):\n{}".format(WatchedMovie, Recommed_Top_Num, recommendMovie_hybrid))



md.to_csv('./md.csv')
smd.to_csv('./MovieData.csv')
ratings.to_csv('./Ratings.csv')
id_map.to_csv('./MovieID_map.csv')
