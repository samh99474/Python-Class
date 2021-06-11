from DB.DBConnection import DBConnection
import json

class MovieData_Table:

    def insert_a_Movie(self,MovieName, Movie_Overview, Movie_release_date, Movie_runtime, Movie_spoken_languages, 
    Movie_release_year = int(), Movie_adult = False, Movie_genres = list(), Movie_cast = list(), Movie_crew = list(), 
    Movie_keywords = list()):

        adult = Movie_adult
        belongs_to_collection = str()
        budget = int()
        genres = Movie_genres
        imdb_id = str()
        original_language = "en"
        original_title = MovieName
        overview = Movie_Overview
        popularity = int()
        production_companies = str()
        production_countries = str()
        release_date = Movie_release_date
        runtime = Movie_runtime
        spoken_languages = Movie_spoken_languages
        status = "Released"
        tagline = str()
        title = MovieName
        video = False
        vote_average = int()
        vote_count = int()
        year = Movie_release_year
        cast = Movie_cast
        crew = Movie_crew
        keywords = Movie_keywords
        #cast_size = len(cast)
        #crew_size = len(crew)
        #Movie_director = "Movie_director"
        #director = [Movie_director, Movie_director, Movie_director]
        #soup = ' '.join(keywords + cast + director + genres)
        
        command = "SELECT MAX(id) FROM MovieData_Table;"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            id_record_from_db = cursor.fetchall()
            for row in id_record_from_db:
                id = row[0] + 1

        command = "INSERT INTO MovieData_Table VALUES  ('{}','{}',{},'{}',{},'{}','{}','{}','{}',{},'{}','{}','{}',{},'{}','{}','{}','{}','{}',{},{},{},'{}','{}','{}');".format(
        adult, belongs_to_collection, budget, json.dumps(genres), id, imdb_id, original_language, original_title, overview, popularity, production_companies
        , production_countries, release_date, runtime, spoken_languages, status, tagline, title, video, vote_average, vote_count, year, json.dumps(cast), str(json.dumps(crew))
        , json.dumps(keywords))


        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def select_a_movie_all_info(self, ID):
        command = "SELECT * FROM MovieData_Table WHERE id='{}';".format(ID)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [dict(row) for row in record_from_db]

    def select_a_ID(self, MovieName):
        command = "SELECT * FROM MovieData_Table WHERE title='{}';".format(MovieName)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['id'] for row in record_from_db]
    
    def select_a_Movie_Name(self, ID):
        command = "SELECT * FROM MovieData_Table WHERE id={};".format(ID)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['title'] for row in record_from_db]
    
    def select_a_Movie_Genres(self, ID):
        command = "SELECT * FROM MovieData_Table WHERE id='{}';".format(ID)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['genres'] for row in record_from_db]
    
    def select_a_Movie_Overview(self, ID):
        command = "SELECT * FROM MovieData_Table WHERE id='{}';".format(ID)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['overview'] for row in record_from_db]
    
    def select_a_Movie_VoteAverage(self, ID):
        command = "SELECT * FROM MovieData_Table WHERE id='{}';".format(ID)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['vote_average'] for row in record_from_db]
    
    def select_a_Movie_VoteCount(self, ID):
        command = "SELECT * FROM MovieData_Table WHERE id='{}';".format(ID)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['vote_count'] for row in record_from_db]
    
    def select_all_Movie_Info(self):
        command = "SELECT * FROM MovieData_Table;"

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [dict(row) for row in record_from_db]

    def delete_a_movie(self, ID):
        command = "DELETE FROM MovieData_Table WHERE id='{}';".format(ID)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def update_a_Movie_Title(self, ID, NewTitle):
        command = "UPDATE MovieData_Table SET title='{}' WHERE id='{}';".format(NewTitle, ID)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def update_a_Movie_Overview(self, ID, changed_Overview):
        command = "UPDATE MovieData_Table SET overview='{}' WHERE id='{}';".format(changed_Overview, ID)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
       