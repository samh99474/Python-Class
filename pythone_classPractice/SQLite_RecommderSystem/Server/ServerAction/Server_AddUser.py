from DB.User_info_Table import User_info_Table

class Server_AddUser:

    def __init__(self):
        print("initialized")

    def execute(self, parameters):
        # init
        status = False
        try:
            for info in parameters:
                
                user_id = User_info_Table().select_a_userId(info["userName"])
                if(len(user_id)==0):
                    User_info_Table().insert_a_user(info["userName"])
                    user_id = User_info_Table().select_a_userId(info["userName"])

                    status = True
                else:
                    print("SQL student_id: {}".format(user_id))
                    status = False

        except Exception as e:  # 若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))

        if(status == True):
            #StudentInfoProcessor().restore_student_file(self.student_dict)   #新資料結合舊資料成功後，存檔
            reply_msg = {'status': "OK", 'parameters': parameters}
        else:
            reply_msg = {'status': "Fail", 'parameters': parameters, 'reason': "The name already exists."}
        return reply_msg