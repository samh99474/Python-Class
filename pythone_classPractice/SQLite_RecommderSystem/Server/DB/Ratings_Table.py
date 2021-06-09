from DB.DBConnection import DBConnection


class Ratings_Table:
    def insert_a_rating(self, userId:int, movieId:int, rating:float, timestamp:int):
        command = "INSERT INTO Ratings_Table VALUES  ({},{},'{}',{});".format(userId, movieId, rating, timestamp)
            
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def select_a_rating(self, userId:int, movieId:int):
        command = "SELECT * FROM Ratings_Table WHERE userId ='{}' AND movieId ='{}';".format(userId, movieId)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['rating'] for row in record_from_db], [row['timestamp'] for row in record_from_db]
    
    def select_a_User_all_ratings(self, userId:int):
        command = "SELECT * FROM Ratings_Table WHERE userId ='{}';".format(userId)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['rating'] for row in record_from_db], [row['timestamp'] for row in record_from_db]
    
    def select_all_Users_ratings(self):
        command = "SELECT * FROM Ratings_Table;"

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['userId'] for row in record_from_db], [row['movieId'] for row in record_from_db], [row['rating'] for row in record_from_db], [row['timestamp'] for row in record_from_db]

    def delete_a_rating(self, userId:int, movieId:int):
        command = "DELETE FROM Ratings_Table WHERE userId='{}' AND movieId='{}';".format(userId, movieId)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
    
    def delete_a_user_all_ratings(self, userId:int):
        command = "DELETE FROM Ratings_Table WHERE userId='{}';".format(userId)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()


    def update_a_rating(self, userId:int, movieId:int, rating:float, timestamp:int):
        command = "UPDATE Ratings_Table SET rating='{}', timestamp='{}' WHERE userId='{}' AND movieId='{}';".format(rating, timestamp, userId, movieId)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
       