class Server_PrintAll:

    def __init__(self, student_dict):
        self.student_dict = student_dict

    def execute(self, parameters):
        status = True
        if(status == True):
            reply_msg = {'status': "OK", 'parameters': self.student_dict}
        else:
            reply_msg = {'status': "Fail",
                        'parameters': "", 'reason': "Fail to show."}

        return self.student_dict, reply_msg