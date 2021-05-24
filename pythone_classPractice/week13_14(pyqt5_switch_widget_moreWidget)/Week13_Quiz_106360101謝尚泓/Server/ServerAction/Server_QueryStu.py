from DB.StudentInfoTable import StudentInfoTable
from DB.SubjectInfoTable import SubjectInfoTable
class Server_QueryStu:
    
    def __init__(self):
        print("initialized")

    def execute(self, parameters):
        # init
        has_item = False
        status = False
        student_dict = dict()
        try:
            for new_student_dict_name, new_student_dict_info in parameters.items():
                student_dict[ new_student_dict_name ] = {}  #建立學生字典

                student_id = StudentInfoTable().select_a_student_id(new_student_dict_name)
                if(len(student_id)==0):
                    has_item = False
                    status = False
                else:
                    student_subject = SubjectInfoTable().select_a_subject(student_id[0])
                    for j in range(len(student_subject)):
                        student_score = SubjectInfoTable().select_a_score(student_id[0], student_subject[j])

                        student_dict[ new_student_dict_name ][ student_subject[j] ] = student_score[0] #建立學生-科目分數字典完成(nested dictionary)
                    print("SQL student_id: {}".format(student_id))
                    has_item = True
                    status = True

        except Exception as e:  # 若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))

        if(status == True): 
            reply_msg = {'status': "OK", 'parameters': student_dict}    #回傳欲query查詢的學生資訊 Nested Dictionary
        else:
            reply_msg = {'status': "Fail", 'parameters': dict(), 'reason': "The name is not found."}
        return reply_msg
