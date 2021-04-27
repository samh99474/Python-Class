class Server_QueryStu:
    
    def __init__(self, student_dict):
        self.student_dict = student_dict

    def execute(self, parameters):
        # init
        has_item = False
        status = False
        try:
            for student_dict_name, student_dict_info in self.student_dict.items():
                # message['parameters'] 是dict
                for new_student_dict_name, new_student_dict_info in parameters.items():
                    if(student_dict_name == new_student_dict_name):  # 已存在Name
                        has_item = True
                        status = True

        except Exception as e:  # 若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))

        if(status == True): 
            reply_msg = {'status': "OK", 'parameters': self.student_dict}
        else:
            reply_msg = {'status': "Fail", 'parameters': dict(), 'reason': "The name is not found."}
        return self.student_dict, reply_msg
