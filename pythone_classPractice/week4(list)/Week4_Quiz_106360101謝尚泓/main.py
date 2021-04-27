import add_stu, del_stu, modify_stu, print_all
#學生: 謝尚泓 106360101
#執行方式: 在terminal 打python ./main.py
#
"""
學習list
"""
def main():
    ## NOTE: NO if else elif judgements are allowed in the main function !!!!
    global student_list
    student_list = read_student_file()
    select_result = 0

    while select_result != 4:
        # call main functions in add_stu, del_stu, modify_stu, print_all here
        function = [add_stu.main, del_stu.main, modify_stu.main, print_all.main] #list 中可以存放Function，然後下面再呼叫
        try:
            select_result = print_menu()
            student_list = function[int(select_result)](student_list)

        except Exception as e:      #若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))
        
        """
        select_result = print_menu()
        if select_result == 0:
            add_stu.main(student_list)
        elif select_result == 1:
            del_stu.main(student_list)
        elif select_result == 2:
            modify_stu.main(student_list)
        elif select_result == 3:
            print_all.main(student_list)
        else:
            print ("No such selection")
        """
    
    restore_student_file(student_list)
    

def read_student_file():
    student_list = list()
    try:
        with open("student_list.txt", "r") as fp:
            for line in fp:
                if len(line) > 0:
                    line = line.rstrip("\n").split(":")
                    student_list.append([line[0], float(line[1])])
    
    except IOError:
        print('An error occured trying to read the file.')
    except: pass

    return student_list

def restore_student_file(student_list):
    # restore student list to file here

    restore_student = ""
    try:
        for i in range(len(student_list)):
            restore_student = restore_student + str(student_list[i][0]) + ":" + str(student_list[i][1]) + "\n"

        with open('./student_list.txt', 'w') as f:
            f.write(restore_student)
            restore_success = True
            #To append data to a file use the 'a' or 'a+' mode 

    except Exception as e:      #若try有錯誤，則執行except
        print("The exception {} occurs.".format(e))
        restore_success = False

    finally:                    #不管try有沒有錯誤，最後一定會執行final
        if(restore_success == True):
            print("存檔成功")
        else:
            print("存檔失敗")
        print("Execution result is {}".format(restore_success))
        return student_list

def print_menu():
    print()
    print("================== Menu ==================")
    print("0. Add a student's name and score")
    print("1. Delete a student")
    print("2. Modify a student's score")
    print("3. Print all")
    print("4. Exit")
    selection = int(input("Please select: "))

    return selection

main()