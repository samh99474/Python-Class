def main(student_dict):
    try:
        subject = ""
        score = 0
        current_subjects = []
        success = False

        print("修改學生姓名和分數")
        name = str(input("  Please input a student's name: "))
        has_item = False
        has_subject = False
        for student_dict_name, student_dict_info in student_dict.items():
            if(student_dict_name == name):
                has_item = True
                break   #student_dict.items()之info name 停止在輸入的name，才不會一直跑下去跑到錯誤(最後)的item
        
        if(has_item == False):
            print("\nThe name {} is not found".format(name))
            success = False
        else:
            for key in student_dict_info:
                current_subjects.append(key)

            print("current subjects are {}".format(current_subjects))
            subject = str(input("  Please input a subject you want to change: "))
            for i in current_subjects:
                if(student_dict_name == name):
                    has_subject = True
            while score >= 0:
                try:
                    if(has_subject == False):           #若沒有此subject，則可新增
                        score = int(input("Add a new subject for {} please input {} score or < 0 for discarding the subject:".format(name, subject)))
                        if(score < 0):
                            score = 0                       # initailize score
                            break
                        student_dict[name][subject] = score # 都成功即可寫入進去student_dict
                        success = True
                        break
                        
                    else:                               #若有此subject，則更改
                        score = int(input("Please input {}'s new score:".format(subject)))
                        if(score < 0):
                            score = 0                       # initailize score
                            break
                        student_dict[name][subject] = score # 都成功即可寫入進去student_dict
                        success = True
                        break
                    
                except: 
                    success = False
                    pass
        
    except Exception as e:      #若try有錯誤，則執行except
        print("The exception {} occurs.".format(e))
        success = False

    finally:                    #不管try有沒有錯誤，最後一定會執行final
        if(success == True):
            print(student_dict)
            print("修改成功")
        else:
            print("修改失敗")
        print("Execution result is {}".format(success))
        return student_dict

"""student_dict = {'kelly': {'english': 60, 'chinese': 90},
          'apple': {'aa': 62, 'bb': 80}}
main(student_dict)"""