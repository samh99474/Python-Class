from DB.DBConnection import DBConnection


class MovieID_map_Table:
    def insert_a_Movie(self, MovieName, id=int()):
        if( id == None ):
            command = "SELECT MAX(id) FROM MovieID_map_Table;"
            with DBConnection() as connection:
                cursor = connection.cursor()
                cursor.execute(command)
                id_record_from_db = cursor.fetchall()
                for row in id_record_from_db:
                    id = row[0] + 1
        
        command = "SELECT MAX(movieId) FROM MovieID_map_Table;"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            id_record_from_db = cursor.fetchall()
            for row in id_record_from_db:
                movieId = row[0] + 1

        command = "INSERT INTO MovieID_map_Table VALUES  ('{}',{},'{}');".format(id, movieId, MovieName)
            
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def select_a_movieId(self, ID):
        command = "SELECT * FROM MovieID_map_Table WHERE id ='{}';".format(ID)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['movieId'] for row in record_from_db]
    
    def select_a_movieTitle(self, ID):
        command = "SELECT * FROM MovieID_map_Table WHERE id ='{}';".format(ID)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['title'] for row in record_from_db]
    
    def select_a_ID(self, movieTitle):
        command = "SELECT * FROM MovieID_map_Table WHERE title ='{}';".format(movieTitle)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['id'] for row in record_from_db]
    
    def select_all_MovieID_map(self):
        command = "SELECT * FROM MovieID_map_Table;"

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['id'] for row in record_from_db], [row['movieId'] for row in record_from_db], [row['title'] for row in record_from_db]

    def delete_a_Movie(self, ID):
        command = "DELETE FROM MovieID_map_Table WHERE id='{}';".format(ID)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def update_a_Movie_Title(self, ID, NewTitle):
        command = "UPDATE MovieID_map_Table SET title={} WHERE id='{}';".format(NewTitle, ID)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
       