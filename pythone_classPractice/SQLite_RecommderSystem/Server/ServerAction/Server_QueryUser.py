from DB.User_info_Table import User_info_Table
class Server_QueryUser:
    
    def __init__(self):
        print("initialized")

    def execute(self, parameters):
        # init
        has_item = False
        status = False
        user_dict = dict()
        user_list = list()
        try:
            for info in parameters:
                user_dict["userName"] = info["userName"]  #建立學生字典

                userId = User_info_Table().select_a_userId(info["userName"])
                if(len(userId)==0):
                    has_item = False
                    status = False
                else:
                    user_dict["userId"] = userId[0]
                    print("SQL student_id: {}".format(userId))
                    has_item = True
                    status = True
                user_list.append(user_dict)

        except Exception as e:  # 若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))

        if(status == True): 
            reply_msg = {'status': "OK", 'parameters': user_list}    #回傳欲query查詢的學生資訊 Nested Dictionary
        else:
            reply_msg = {'status': "Fail", 'parameters': user_list, 'reason': "The name is not found."}
        return reply_msg
