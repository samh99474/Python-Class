from sqlite3.dbapi2 import Timestamp
from DBConnection import DBConnection
from DBInitializer import DBInitializer
from MovieData_Table import MovieData_Table
from MovieID_map_Table import MovieID_map_Table
from Ratings_Table import Ratings_Table
from User_info_Table import User_info_Table

#===================================================== the file is just for testing
DBConnection.db_file_path = "../UserMovie.db"
DBInitializer().execute()

"""Movie_Name = "samh"
print("\Insert Movie: {}\n",format(Movie_Name))
MovieData_Table().insert_a_Movie(Movie_Name,"overview","2021-6-9","600","en",2021,False,['Action','Comedy'],['Sam','GD'],
[{'credit_id': '52fe440ac3a36847f807ee01', 'department': 'Camera', 'gender': 2, 'id': 1657, 'job': 'Director of Photography', 'name': 'Henri Decaë', 'profile_path': None}],
['keyword', 'samurai', 'classic'],"Director")

ID = MovieData_Table().select_a_ID(Movie_Name)
select_Movie_Name = MovieData_Table().select_a_Movie_Name(ID[0])
Movie_Genres = MovieData_Table().select_a_Movie_Genres(ID[0])
print("\nMovieData_Table:\n")
print("Movie_ID: {} , and length = {}".format(ID[0], len(ID)))
print("select_Movie_Name: {} , and length = {}".format(select_Movie_Name[0], len(select_Movie_Name)))
print("Movie_Genres: {} , and length = {}".format(Movie_Genres, len(Movie_Genres)))
#=======================================================================
MovieID_map_Table().insert_a_Movie(select_Movie_Name[0], ID[0])
MovieID_map_ID = MovieID_map_Table().select_a_ID(Movie_Name)
MovieID_map_MovieID = MovieID_map_Table().select_a_movieId(ID[0])
MovieID_map_MovieTitle = MovieID_map_Table().select_a_movieTitle(ID[0])
print("\nMovieID_map_Table:\n")
print("ID: {} , and length = {}".format(MovieID_map_ID[0], len(MovieID_map_ID)))
print("MovieID_map_MovieID: {} , and length = {}".format(MovieID_map_MovieID[0], len(MovieID_map_MovieID)))
print("MovieID_map_MovieTitle: {} , and length = {}".format(MovieID_map_MovieTitle[0], len(MovieID_map_MovieTitle)))

select_Movie_Name = MovieData_Table().select_a_Movie_Name(MovieID_map_ID[0])
print("GET BACK => select_Movie_Name: {} , and length = {}".format(select_Movie_Name[0], len(select_Movie_Name)))
#=======================================================================
User_Name = "sam"
User_ID = 672
rating = 4.5
Timestamp = 1064891129
Ratings_Table().insert_a_rating(User_ID, MovieID_map_MovieID[0], rating, Timestamp)
get_rating = Ratings_Table().select_a_rating(User_ID, MovieID_map_MovieID[0])
print("rating: {} , and length = {}".format(get_rating[0], len(get_rating)))"""
#=======================================================================
UserName = "unknown"
User_info_Table().insert_a_user(UserName)
userId = User_info_Table().select_a_userId(UserName)
userName = User_info_Table().select_a_userName(userId[0])
print("userId: {} , and length = {}".format(userId, len(userId)))
print("userName: {} , and length = {}".format(userName[0], len(userName)))

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
