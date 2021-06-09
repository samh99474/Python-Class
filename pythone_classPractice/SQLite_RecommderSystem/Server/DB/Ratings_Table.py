from DBConnection import DBConnection


class Ratings_Table:
    def insert_a_subject(self, stu_id, subject, score):
        command = "INSERT INTO subject_info VALUES  ({},'{}',{});".format(stu_id, subject, score)
            
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def select_a_subject(self, stu_id):
        command = "SELECT * FROM subject_info WHERE stu_id ='{}';".format(stu_id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['subject'] for row in record_from_db]
    
    def select_a_score(self, stu_id, subject):
        command = "SELECT * FROM subject_info WHERE stu_id ='{}' AND subject ='{}';".format(stu_id, subject)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['score'] for row in record_from_db]
    
    def select_all_subject(self):
        command = "SELECT * FROM subject_info;"

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['stu_id'] for row in record_from_db], [row['subject'] for row in record_from_db], [row['score'] for row in record_from_db]

    def delete_a_subject(self, stu_id):
        command = "DELETE FROM subject_info WHERE stu_id='{}';".format(stu_id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def update_a_score(self, stu_id, subject, new_score):
        command = "UPDATE subject_info SET score={} WHERE stu_id='{}' AND subject='{}';".format(new_score, stu_id, subject)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
       