import json
class DelStu():
    def __init__(self, socket_client):
        self.socket_client = socket_client

    def execute(self):
        try:
            print("刪除學生")
            name = str(input("  Please input a student's name: "))
            has_item = False
            student_dict = dict()
            student_dict[name] = {}

            query_student_dict = dict()
            query_student_dict[name] = {}

            #先查詢query是否存在此學生名稱
            self.socket_client.send_command("query", query_student_dict)
            print("\nclient send data to server => \'command\':{}, \'parameters\':{}".format("query", query_student_dict))

            boolean, result = self.socket_client.wait_response()
            result = json.loads(result) # convert dictionary string to dictionary
            if(result['status'] == "Fail"):
                print("\nThe name {} is not found".format(name))
                has_item = False
                success = False
            else:
                has_item = True
                success = True

            
        except Exception as e:      #若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))
            success = False
        finally:                    #不管try有沒有錯誤，最後一定會執行final
            if(success == True):
                 #=========================== socket_client 傳送指令和資料給server==================
                self.socket_client.send_command("del", student_dict)
                print("\nclient send data to server => \'command\':{}, \'parameters\':{}".format("del", student_dict))

                boolean, result = self.socket_client.wait_response()
                result = json.loads(result) # convert dictionary string to dictionary

                if result['status'] == "OK":
                    print("    delete {} success".format(name))
                    print("刪除成功")
                else:
                    print("    delete {} fail".format(name))
            else:
                print("刪除失敗")
            print("Execution result is {}".format(success))
            return student_dict