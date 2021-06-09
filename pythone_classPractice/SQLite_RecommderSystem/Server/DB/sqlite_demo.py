from DBConnection import DBConnection
from DBInitializer import DBInitializer
from MovieData_Table import MovieData_Table
from MovieID_map_Table import MovieID_map_Table
from Ratings_Table import Ratings_Table

#===================================================== the file is just for testing
DBConnection.db_file_path = "../UserMovie.db"
DBInitializer().execute()

Movie_Name = "Toy Story"
#subject = "python"
#StudentInfoTable().insert_a_student(studentName)

Movie_ID = MovieData_Table().select_a_Movie_ID("Toy Story")
select_Movie_Name = MovieData_Table().select_a_Movie_Name(Movie_ID[0])
Movie_Genres = MovieData_Table().select_a_Movie_Genres(Movie_ID[0])
print("Movie_ID: {} , and length = {}".format(Movie_ID[0], len(Movie_ID)))
print("select_Movie_Name: {} , and length = {}".format(select_Movie_Name[0], len(select_Movie_Name)))
print("Movie_Genres: {} , and length = {}".format(Movie_Genres, len(Movie_Genres)))

#MovieData_Table().insert_a_Movie("sam","overview","2021-6-9","600","en",2021,False,['Action','Comedy'],['Sam','GD'])

MovieData_Table().insert_a_Movie("sam","overview","2021-6-9","600","en",2021,False,['Action','Comedy'],['Sam','GD'],
[{'credit_id': '52fe440ac3a36847f807ee01', 'department': 'Camera', 'gender': 2, 'id': 1657, 'job': 'Director of Photography', 'name': 'Henri Decaë', 'profile_path': None}],
['keyword', 'samurai', 'classic'],"Director")

"""student_id, student_subject, student_score = SubjectInfoTable().select_all_subject()
print("student_id: {} , and length = {}".format(student_id, len(student_id)))
print("student_subject: {} , and length = {}".format(student_subject, len(student_subject)))
print("student_score: {} , and length = {}".format(student_score, len(student_score)))"""

"""for i in range(len(student_id)):
    print("\nStudent ID: {}, Student Name: {}".format(student_id[i], student_name[i]))
    student_subject = SubjectInfoTable().select_a_subject(student_id[i])
    for j in range(len(student_subject)):
        student_score = SubjectInfoTable().select_a_score(student_id[i], student_subject[j])
        print("\nStudent Subject: {}, Student Score: {}".format(student_subject[j], student_score))
"""

"""student_id = StudentInfoTable().select_a_student(studentName)
print("student_id: {} , and length = {}".format(student_id, len(student_id)))"""

"""for i in range(2):
    SubjectInfoTable().insert_a_student(student_id[0], subject, 100)"""

"""for i in range(len(student_id)):
    StudentInfoTable().delete_a_student(student_id[i])"""
# StudentInfoTable().update_a_student("1", "Test")
