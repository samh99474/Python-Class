def main(student_list):
    success = True
    try:
        print("更新資料")
        name = str(input("  Please input a student's name: "))
        new_score = int(input("  Please input {}'s new score: ".format(name)))
    except Exception as e:      #若try有錯誤，則執行except
        print("The exception {} occurs.".format(e))
        success = False
    else:                       #若try沒有錯誤，則執行else
       for i in range(len(student_list)):
            if name == str(student_list[i][0]):
                student_list[i][1] = new_score
                success = True
    finally:                    #不管try有沒有錯誤，最後一定會執行final
        #print(student_list)
        if(success == True):
            print("修改成功，{}分數變為{}".format(name, new_score))
        else:
            print("修改失敗")

        print("Execution result is {}".format(success))
        return student_list
"""
student_list = [["dog",30],["cat",80]]
main(student_list)
"""
