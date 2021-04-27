def main(student_list):
    success = True
    try:
        print("刪除學生")
        name = str(input("  Please input a student's name: "))
    except Exception as e:      #若try有錯誤，則執行except
        print("The exception {} occurs.".format(e))
        success = False
    else:                       #若try沒有錯誤，則執行else
       for i in range(len(student_list)):
            if name == str(student_list[i][0]):
                student_list.pop(i)
                success = True
            else:
                success = False
    finally:                    #不管try有沒有錯誤，最後一定會執行final
        print(student_list)
        if(success == True):
            print("刪除{}成功".format(name))
        else:
            print("刪除失敗")
        print("Execution result is {}".format(success))
        return student_list
"""
student_list = [["dog",30],["cat",80]]
main(student_list)
"""