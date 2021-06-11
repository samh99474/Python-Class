import json
class QueryMovie():
    def __init__(self, socket_client):
        self.socket_client = socket_client

    def execute(self):
        try:
            query_movie_dict = dict()
            query_movie_list = list()

            print("請輸入欲查詢之電影id")
            movieId = int(input("  Please input a movie's id: "))
            query_movie_dict["id"] = movieId

            query_movie_list.append(query_movie_dict)

            #先查詢query是否存在此用戶名稱
            self.socket_client.send_command("queryMovie", query_movie_list)
            print("\nclient send data to server => \'command\':{}, \'parameters\':{}".format("queryMovie", query_movie_list))
            boolean, result = self.socket_client.wait_response()
            result = json.loads(result) # convert dictionary string to dictionary
            if result['status'] == "Fail":
                print("此電影ID不存在")
                success = False
            else:
                print("此電影ID存在")
                success = True
        
        except Exception as e:      #若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))
            success = False
        finally:                    #不管try有沒有錯誤，最後一定會執行final
            if(success == True):
                print("查詢成功")
            else:
                print("查詢失敗")
            print("Execution result is {}".format(success))