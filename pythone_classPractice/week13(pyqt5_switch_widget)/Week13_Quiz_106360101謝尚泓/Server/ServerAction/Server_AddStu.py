from DB.StudentInfoTable import StudentInfoTable
from DB.SubjectInfoTable import SubjectInfoTable

class Server_AddStu:

    def __init__(self):
        print("initialized")

    def execute(self, parameters):
        # init
        has_item = False
        status = False
        try:
            for new_student_dict_name, new_student_dict_info in parameters.items():
                student_id = StudentInfoTable().select_a_student_id(new_student_dict_name)
                if(len(student_id)==0):
                    StudentInfoTable().insert_a_student(new_student_dict_name)
                    student_id = StudentInfoTable().select_a_student_id(new_student_dict_name)

                    for subject in new_student_dict_info:
                        score = new_student_dict_info[subject]
                        SubjectInfoTable().insert_a_subject(student_id[0], subject, score) #insert a student => (id, subject, score)
                        print(subject + ':', score)    #subject:score
                    has_item = False
                    status = True
                else:
                    print("SQL student_id: {}".format(student_id))
                    has_item = True
                    status = False

        except Exception as e:  # 若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))

        if(status == True):
            #StudentInfoProcessor().restore_student_file(self.student_dict)   #新資料結合舊資料成功後，存檔
            reply_msg = {'status': "OK", 'parameters': parameters}
        else:
            reply_msg = {'status': "Fail", 'parameters': "", 'reason': "The name already exists."}
        return reply_msg
