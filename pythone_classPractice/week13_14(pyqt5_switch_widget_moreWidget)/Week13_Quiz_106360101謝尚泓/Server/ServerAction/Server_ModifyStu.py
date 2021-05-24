from DB.StudentInfoTable import StudentInfoTable
from DB.SubjectInfoTable import SubjectInfoTable
class Server_ModifyStu:

    def __init__(self):
        print("initialized")
    def execute(self, parameters):
        # init
        has_item = False
        status = False
        try:
            # Update score into existing subject
            for new_student_dict_name, new_student_dict_info in parameters.items():
                student_id = StudentInfoTable().select_a_student_id(new_student_dict_name)
                for subject in new_student_dict_info:
                    score = new_student_dict_info[subject]
                    
                    #check if each subject has exist in original SQLite DataBase
                    sqlite_subject = SubjectInfoTable().select_a_subject(student_id[0])
                    if subject in sqlite_subject:   #若欲更新的subject 已經在SQLite，則update方式更新
                        SubjectInfoTable().update_a_score(student_id[0], subject, score)
                    else:                           #若欲更新的subject 不存在SQLite，則insert方式新增
                        SubjectInfoTable().insert_a_subject(student_id[0], subject, score)
                    print(subject + ':', score)    #subject:score
                has_item = True
                status = True
            
        except Exception as e:  # 若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))

        if(status == True):
            #StudentInfoProcessor().restore_student_file(self.student_dict)   #新資料結合舊資料成功後，存檔
            reply_msg = {'status': "OK", 'parameters': parameters}
        else:
            reply_msg = {'status': "Fail", 'parameters': "", 'reason': "The name already exists."}
        return reply_msg