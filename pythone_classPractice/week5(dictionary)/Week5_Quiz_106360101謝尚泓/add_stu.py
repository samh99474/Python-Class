def main(student_dict):
    try:
        print("新增學生姓名和分數")
        name = str(input("  Please input a student's name: "))
        subject = ""
        score = 0
        has_item = False

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
                        for student_dict_name, student_dict_info in student_dict.items():
                            if(student_dict_name == name):
                                has_item = True
                                break   #student_dict.items()之info name 停止在輸入的name，才不會一直跑下去跑到錯誤(最後)的item
                            else:
                                has_item = False

                        if(has_item == False):
                            student_dict[name] = {}                #若沒此學生，則建立學生

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
            print(student_dict)
            print("新增成功")
        else:
            print("新增失敗")
        print("Execution result is {}".format(success))
        return student_dict

"""student_dict = {}
main(student_dict)"""