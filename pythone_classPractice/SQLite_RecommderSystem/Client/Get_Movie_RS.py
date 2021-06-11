import json
class Get_Movie_RS():
    def __init__(self, socket_client):
        self.socket_client = socket_client

    def execute(self):
        try:
            query_user_list = list()
            RS_dict = dict()

            print("輸入用戶姓名")
            userName = str(input("  Please input a user's name: "))
            RS_dict["userName"] = userName

            query_user_list.append(RS_dict)

            print("輸入用戶ID")
            userId = str(input("  Please input a user's ID: "))
            query_user_dict = dict()
            query_user_dict["userId"] = userId
            RS_dict["userId"] = userId

            print("輸入電影Name")
            movieTitle = str(input("  Please input a movies's Name: "))
            RS_dict["movieTitle"] = movieTitle

            print("輸入電影ID")
            id = int(input("  Please input a movies's ID: "))
            RS_dict["id"] = id

            print("輸入欲得到之推薦數量:")
            Recommed_Top_Num = int(input("  Please input a Recommed_Top_Num: "))
            RS_dict["Recommed_Top_Num"] = Recommed_Top_Num

            RS_list_info = list()
            RS_list_info.append(RS_dict)

            print("輸入欲使用之推薦方法: \n方法一、contentBased \n 方法二、hybrid")
            RS_method = str(input("  Please input contentBased or hybrid : "))
            RS_dict["RS_method"] = RS_method

            RS_list_info = list()
            RS_list_info.append(RS_dict)

            #先查詢query是否存在此學生名稱
            self.socket_client.send_command("queryUser", query_user_list)
            print("\nclient send data to server => \'command\':{}, \'parameters\':{}".format("query", query_user_list))

            boolean, result = self.socket_client.wait_response()
            result = json.loads(result) # convert dictionary string to dictionary

            if result['status'] == "Fail":
                print("此用戶名稱不存在")
                success = False
            else:
                print("此用戶名稱存在")
                success = True
        
        except Exception as e:      #若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))
            success = False
        finally:                    #不管try有沒有錯誤，最後一定會執行final
            if(success == True):
                #=========================== socket_client 傳送指令和資料給server==================
                self.socket_client.send_command("RS", RS_list_info)
                print("\nclient send data to server => \'command\':{}, \'parameters\':{}".format("RS", RS_list_info))

                boolean, result = self.socket_client.wait_response()
                result = json.loads(result) # convert dictionary string to dictionary

                if result['status'] == "OK":
                    print("    get movie recommendation {} success".format(result["parameters"]))
                    print("推薦電影成功")
                else:
                    print("    get movie recommendation {} fail".format(result["parameters"]))
            
            else:
                print("推薦電影失敗")
            print("Execution result is {}".format(success))
            return query_user_dict