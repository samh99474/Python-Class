from DB.StudentInfoTable import StudentInfoTable
from DB.SubjectInfoTable import SubjectInfoTable
class Server_PrintAll:

    def __init__(self):
        print("initialized")

    def execute(self, parameters):
        status = True
        student_dict = dict()

        student_id, student_name = StudentInfoTable().select_all_student_id()

        for i in range(len(student_id)):
            print("\nStudent ID: {}, Student Name: {}".format(student_id[i], student_name[i]))
            student_dict[student_name[i]] = {}

            student_subject = SubjectInfoTable().select_a_subject(student_id[i])
            for j in range(len(student_subject)):
                student_score = SubjectInfoTable().select_a_score(student_id[i], student_subject[j])

                student_dict[ student_name[i] ][ student_subject[j] ] = student_score[0]
                print("\nStudent Subject: {}, Student Score: {}".format(student_subject[j], student_score[0]))
                
        if(status == True):
            reply_msg = {'status': "OK", 'parameters': student_dict}
        else:
            reply_msg = {'status': "Fail",
                        'parameters': "", 'reason': "Fail to show."}

        return reply_msg