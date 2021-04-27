class AddStu():
    def __init__(self, student_dict):
        self.student_dict = student_dict

    def execute(self):
        try:
            print("新增學生姓名和分數")
            name = str(input("  Please input a student's name: "))
            subject = ""
            score = 0

            while subject != "exit":
                try:
                    subject = str(input("  Please input a subject or exit for ending: "))
                    if(subject == "exit"):                      # subject == "exit" exit for ending
                        if(self.student_dict[name] == {}):
                            del self.student_dict[name]              # 清空學生 完全沒subject的字典
                            success = False
                        break
                    while score >= 0:
                        try:
                            score = int(input("  Please input {}'s {} score or < 0 for discarding the subject: ".format(name, subject)))  #盡量用format轉換格式
                            if(score < 0):
                                score = 0                       # initailize score
                                break
                            self.student_dict[name][subject] = score # 都成功即可寫入進去student_dict
                            success = True
                            break
                        except: pass
                except:
                    pass
        
        except Exception as e:      #若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))
            success = False
        finally:                    #不管try有沒有錯誤，最後一定會執行final
            if(success == True):
                print(self.student_dict)
                print("新增成功")
            else:
                print("新增失敗")
            print("Execution result is {}".format(success))
            return self.student_dict