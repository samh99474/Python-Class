from DB.DBConnection import DBConnection


class User_info_Table:
    def insert_a_user(self, userName:str):
        command = "INSERT INTO User_info_Table (userName) VALUES  ('{}');".format(userName)
            
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def select_a_userId(self, userName:str):
        command = "SELECT * FROM User_info_Table WHERE userName='{}';".format(userName)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['userId'] for row in record_from_db]
    
    def select_a_userName(self, userId:int):
        command = "SELECT * FROM User_info_Table WHERE userId='{}';".format(userId)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['userName'] for row in record_from_db]
    
    def select_all_users(self):
        command = "SELECT * FROM User_info_Table;"

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['userId'] for row in record_from_db], [row['userName'] for row in record_from_db]

    def delete_a_user(self, userId:int):
        command = "DELETE FROM User_info_Table WHERE userId='{}';".format(userId)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def update_a_userName(self, userId:int, new_userName:str):
        command = "UPDATE User_info_Table SET userName='{}' WHERE userId='{}';".format(new_userName, userId)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
       