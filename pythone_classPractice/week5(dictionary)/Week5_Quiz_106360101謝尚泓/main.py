import add_stu, del_stu, modify_stu, print_all
import pickle
#學生: 謝尚泓 106360101
#執行方式: 在terminal 打python ./main.py 或 Ctrl+Alt+N
#
"""
學習Dictionary
Nested dictionary
https://www.programiz.com/python-programming/nested-dictionary
"""
action_list = {
    "add": add_stu.main, 
    "del": del_stu.main, 
    "modify": modify_stu.main, 
    "show": print_all.main
}

def main():
    student_dict = read_student_file()
    select_result = "initial"

    while select_result != "exit":
        select_result = print_menu()
        try:
            student_dict = action_list[select_result](student_dict)
        except:
            pass
    
    restore_student_file(student_dict)

def read_student_file():
    student_dict = dict()
    try:
        with open("student_list.txt", "rb") as fp:
            student_dict = pickle.load(fp)
    except:
        pass

    return student_dict

def restore_student_file(student_dict):
    with open("student_list.txt", "wb") as fp:
        pickle.dump(student_dict, fp)

def print_menu():
    print()
    print("add: Add a student's name and score")
    print("del: Delete a student")
    print("modify: Modify a student's score")
    print("show: Print all")
    print("exit: Exit")
    selection = input("Please select: ")

    return selection

main()