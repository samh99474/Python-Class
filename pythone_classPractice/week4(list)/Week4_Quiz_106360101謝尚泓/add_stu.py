def main(student_list):
    try:
        print("新增學生")
        name = str(input("  Please input a student's name: "))
        score = int(input("  Please input {}'s score: ".format(name)))  #盡量用format轉換格式
    except Exception as e:      #若try有錯誤，則執行except
        print("The exception {} occurs.".format(e))
        success = False
    else:                       #若try沒有錯誤，則執行else
        student_list.append([name, score])
        print("成功新增學生:"+name+", 分數:"+str(score))
        #print(student_list)
        success = True
    finally:                    #不管try有沒有錯誤，最後一定會執行final
        if(success == True):
            print("新增成功")
        else:
            print("新增失敗")
        print("Execution result is {}".format(success))
        return student_list
"""
student_list = [["dog",30]]
main(student_list)
"""

