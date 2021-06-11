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
from Recommender.contentBased_RS import contentBased_RS
from Recommender.hybrid_RS import hybrid_RS
import warnings; warnings.simplefilter('ignore')

action_list = {
    "contentBased": contentBased_RS,
    "hybrid": hybrid_RS,
}
class main_recommender:
    def __init__(self):
        print("main_recommender initialized")

    def execute(self, Watched_Movie_title:str=None, Watched_Movie_ID:int=None, userId:int=None, RS_method="contentBased", Recommed_Top_Num=20):
        
        self.RS_result = action_list[RS_method]().execute(userId=userId, Watched_Movie_title=Watched_Movie_title, Watched_Movie_ID=Watched_Movie_ID, 
        Recommed_Top_Num=Recommed_Top_Num)
        return self.RS_result

"""main_RS = main_recommender()
result = main_RS.execute(Watched_Movie_title="Toy Story", Watched_Movie_ID=863, userId=1, RS_method="hybrid", Recommed_Top_Num=20)
print(result)
"""
