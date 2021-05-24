from DB.StudentInfoTable import StudentInfoTable
from DB.SubjectInfoTable import SubjectInfoTable
class Server_DelStu:

    def __init__(self):
        print("initialized")

    def execute(self, parameters):
        # init
        status = False
        try:
            for new_student_dict_name, new_student_dict_info in parameters.items():
                student_id = StudentInfoTable().select_a_student_id(new_student_dict_name)

                StudentInfoTable().delete_a_student(student_id[0])
                SubjectInfoTable().delete_a_subject(student_id[0])
                status = True

        except Exception as e:  # 若try有錯誤，則執行except
            status = False
            print("The exception {} occurs.".format(e))

        if(status == True):
            #StudentInfoProcessor().restore_student_file(self.student_dict)   #新資料結合舊資料成功後，存檔
            reply_msg = {'status': "OK", 'parameters': parameters}
        else:
            reply_msg = {'status': "Fail", 'parameters': "", 'reason': "The name already exists."}
        return reply_msg
