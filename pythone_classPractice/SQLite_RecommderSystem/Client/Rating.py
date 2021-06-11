import json
class Rating():
    def __init__(self, socket_client):
        self.socket_client = socket_client

    def execute(self):
        try:
            rating_dict = dict()
            rating_list = list()
            print("用戶姓名")
            userName = str(input("  Please input a user's name: "))
            rating_dict["userName"] = userName

            print("用戶ID")
            userId = str(input("  Please input a user's ID: "))
            rating_dict["userId"] = userId

            print("請輸入電影ID")
            movieId = int(input("  Please input a movieId: "))
            rating_dict["movieId"] = movieId

            print("請輸入電影評分 1~5 分")
            rating = int(input("  Please input a rating: "))
            rating_dict["rating"] = rating

            rating_list.append(rating_dict)

            #先查詢query是否存在此用戶名稱
            self.socket_client.send_command("queryUser", rating_list)
            print("\nclient send data to server => \'command\':{}, \'parameters\':{}".format("query", rating_list))
            boolean, result = self.socket_client.wait_response()
            result = json.loads(result) # convert dictionary string to dictionary
            if result['status'] == "Fail":
                print("此名稱不存在，您不可以新增此學生")
                success = False
            else:
                print("此名稱存在，您可以新增此學生")
                success = True
        
        except Exception as e:      #若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))
            success = False
        finally:                    #不管try有沒有錯誤，最後一定會執行final
            if(success == True):
                #=========================== socket_client 傳送指令和資料給server==================
                self.socket_client.send_command("rating", rating_list)
                print("\nclient send data to server => \'command\':{}, \'parameters\':{}".format("rating", rating_list))

                boolean, result = self.socket_client.wait_response()
                result = json.loads(result) # convert dictionary string to dictionary

                if result['status'] == "OK":
                    print("    Rating {} success".format(result["parameters"]))
                    print("新增成功")
                else:
                    print("    Rating {} fail".format(result["parameters"]))
            
            else:
                print("新增失敗")
            print("Execution result is {}".format(success))
            return rating_list