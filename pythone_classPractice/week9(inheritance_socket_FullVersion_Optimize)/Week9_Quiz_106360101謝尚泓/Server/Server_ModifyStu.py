class Server_ModifyStu:

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
                    if(student_dict_name == new_student_dict_name):  # 存在Name
                        has_item = True
                        status = True
                        self.student_dict.update(parameters)

                """if(len(student_dict.items()) == 0):  # 若原始dict為空，不會有已存在Name的問題，則可以將新data直接merge(update)加入
                    student_dict.update(self.message['parameters'])
                    has_item = False
                    status = True"""

        except Exception as e:  # 若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))

        if(status == True):
            #StudentInfoProcessor().restore_student_file(self.student_dict)   #新資料結合舊資料成功後，存檔
            reply_msg = {'status': "OK", 'parameters': self.student_dict}
        else:
            reply_msg = {'status': "Fail", 'parameters': "", 'reason': "The name already exists."}
        return self.student_dict, reply_msg