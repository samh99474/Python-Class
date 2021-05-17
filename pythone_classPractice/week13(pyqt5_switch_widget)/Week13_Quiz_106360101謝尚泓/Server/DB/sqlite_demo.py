from DB.DBConnection import DBConnection
from DB.DBInitializer import DBInitializer
from DB.StudentInfoTable import StudentInfoTable
from DB.SubjectInfoTable import SubjectInfoTable

#===================================================== the file is just for testing
DBConnection.db_file_path = "example.db"
DBInitializer().execute()

studentName = "cc"
subject = "python"
#StudentInfoTable().insert_a_student(studentName)

student_id, student_name = StudentInfoTable().select_all_student_id()
print("student_id: {} , and length = {}".format(student_id, len(student_id)))
print("student_name: {} , and length = {}".format(student_name, len(student_name)))

"""student_id, student_subject, student_score = SubjectInfoTable().select_all_subject()
print("student_id: {} , and length = {}".format(student_id, len(student_id)))
print("student_subject: {} , and length = {}".format(student_subject, len(student_subject)))
print("student_score: {} , and length = {}".format(student_score, len(student_score)))"""

for i in range(len(student_id)):
    print("\nStudent ID: {}, Student Name: {}".format(student_id[i], student_name[i]))
    student_subject = SubjectInfoTable().select_a_subject(student_id[i])
    for j in range(len(student_subject)):
        student_score = SubjectInfoTable().select_a_score(student_id[i], student_subject[j])
        print("\nStudent Subject: {}, Student Score: {}".format(student_subject[j], student_score))

"""student_id = StudentInfoTable().select_a_student(studentName)
print("student_id: {} , and length = {}".format(student_id, len(student_id)))"""

"""for i in range(2):
    SubjectInfoTable().insert_a_student(student_id[0], subject, 100)"""

"""for i in range(len(student_id)):
    StudentInfoTable().delete_a_student(student_id[i])"""
# StudentInfoTable().update_a_student("1", "Test")
