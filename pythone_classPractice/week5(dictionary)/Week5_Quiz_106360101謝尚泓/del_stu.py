def main(student_dict):
    try:
        print("刪除學生")
        name = str(input("  Please input a student's name: "))
        del student_dict[name]
        
    except Exception as e:      #若try有錯誤，則執行except
        print("The exception {} occurs.".format(e))
        success = False
    else:                       #若try沒錯誤會執行else
        success = True
    finally:                    #不管try有沒有錯誤，最後一定會執行final
        if(success == True):
            print("刪除{}成功".format(name))
        else:
            print("刪除失敗")
        print("Execution result is {}".format(success))
        return student_dict
"""
student_dict = {'John': {'english': 60, 'chinese': 90},
          'Marie': {'english': 62, 'chinese': 80}}
main(student_dict)"""


