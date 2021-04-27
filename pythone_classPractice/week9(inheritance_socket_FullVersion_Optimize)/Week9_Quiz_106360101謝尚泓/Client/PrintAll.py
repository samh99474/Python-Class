import json
class PrintAll():
    def __init__(self, socket_client):
        self.socket_client = socket_client

    def execute(self):
        try:
            #=========================== socket_client 傳送指令和資料給server==================
            self.socket_client.send_command("show", dict())
            print("\nclient send data to server => \'command\':{}, \'parameters\':{}".format("show", dict()))

            boolean, result = self.socket_client.wait_response()
            result = json.loads(result) # convert dictionary string to dictionary


            if result['status'] == "OK":
                student_dict = result['parameters']
            
                PrintAll_studentList = "\n==== student list ====\n"
                for student_dict_name, student_dict_info in student_dict.items():
                    PrintAll_studentList += "\nName: " + student_dict_name
                    for key in student_dict_info:
                        PrintAll_studentList += "   subject:" + str(key) + "\'score\':" + str(student_dict_info[key])
                PrintAll_studentList += "\n======================"
                
                print(PrintAll_studentList)
            
        except Exception as e:      #若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))
        

"""student_dict = {'kelly': {'english': 60, 'chinese': 90},
          'apple': {'english': 62, 'chinese': 80}}
x = PrintAll(student_dict).execute()
print(x)"""
                
