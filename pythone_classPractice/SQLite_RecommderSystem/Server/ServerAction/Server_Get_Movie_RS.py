from Recommender.contentBased_RS import contentBased_RS
from Recommender.hybrid_RS import hybrid_RS

RS_action_list = {
    "contentBased": contentBased_RS,
    "hybrid": hybrid_RS,
}

class Server_Get_Movie_RS:
    
    def __init__(self):
        print("initialized")

    def execute(self, parameters):
        # init
        RS_result=list()
        status = False
        try:
            for info in parameters:
                userName = info["userName"]
                userId = info["userId"]
                movieTitle = info["movieTitle"]
                id = info["id"]
                Recommed_Top_Num = info["Recommed_Top_Num"]
                RS_method = info["RS_method"]

            RS_result = RS_action_list[RS_method]().execute(userId=userId, Watched_Movie_title=movieTitle, Watched_Movie_ID=id, 
            Recommed_Top_Num=Recommed_Top_Num)

            status = True

        except Exception as e:  # 若try有錯誤，則執行except
            status = False
            print("The exception {} occurs.".format(e))

        if(status == True):
            #StudentInfoProcessor().restore_student_file(self.student_dict)   #新資料結合舊資料成功後，存檔
            reply_msg = {'status': "OK", 'parameters': RS_result}
        else:
            reply_msg = {'status': "Fail", 'parameters': RS_result, 'reason': "Recommender System Error."}
        return reply_msg
