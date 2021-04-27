import json
class AddStu():
    def __init__(self, socket_client):
        self.socket_client = socket_client

    def execute(self):
        try:
            print("新增學生姓名和分數")
            name = str(input("  Please input a student's name: "))
            subject = ""
            score = 0
            has_item = False
            student_dict = dict()
            query_student_dict = dict()
            query_student_dict[name] = {}

            #先查詢query是否存在此學生名稱
            self.socket_client.send_command("query", query_student_dict)
            print("\nclient send data to server => \'command\':{}, \'parameters\':{}".format("query", query_student_dict))

            boolean, result = self.socket_client.wait_response()
            result = json.loads(result) # convert dictionary string to dictionary

            if result['status'] == "Fail":
                print("此名稱不存在，您可以新增此學生")
                has_item = False
                success = True
            else:
                print("此名稱存在，您不可以新增此學生")
                has_item = True
                success = False
            
            if(has_item == False):  #沒有此學生名稱，才能新增，繼續進行下面處理
                student_dict[name] = {}  
                while subject != "exit":
                    try:
                        subject = str(input("  Please input a subject or exit for ending: "))
                        if(subject == "exit"):                      # subject == "exit" exit for ending
                            if(student_dict[name] == {}):
                                del student_dict[name]              # 清空學生 完全沒subject的字典
                                success = False
                            break
                        while score >= 0:
                            try:
                                score = int(input("  Please input {}'s {} score or < 0 for discarding the subject: ".format(name, subject)))  #盡量用format轉換格式
                                if(score < 0):
                                    score = 0                       # initailize score
                                    break

                                student_dict[name][subject] = score # 都成功即可寫入進去student_dict，建立學生的成績
                                success = True
                                break
                            except Exception as e:      #若try有錯誤，則執行except
                                print("The exception {} occurs.".format(e))
                                success = False
                    except:
                        pass
        
        except Exception as e:      #若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))
            success = False
        finally:                    #不管try有沒有錯誤，最後一定會執行final
            if(success == True):
                #=========================== socket_client 傳送指令和資料給server==================
                self.socket_client.send_command("add", student_dict)
                print("\nclient send data to server => \'command\':{}, \'parameters\':{}".format("add", student_dict))

                boolean, result = self.socket_client.wait_response()
                result = json.loads(result) # convert dictionary string to dictionary

                if result['status'] == "OK":
                    print("    Add {} success".format(student_dict))
                    print("新增成功")
                else:
                    print("    Add {} fail".format(student_dict))
            
            else:
                print("新增失敗")
            print("Execution result is {}".format(success))
            return student_dict