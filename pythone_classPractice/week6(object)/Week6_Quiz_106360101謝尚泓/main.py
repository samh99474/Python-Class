from AddStu import AddStu
from DelStu import DelStu
from ModifyStu import ModifyStu
from PrintAll import PrintAll
from StudentInfoProcessor import StudentInfoProcessor
#學生: 謝尚泓 106360101
#執行方式: 在terminal 打python ./main.py 或 Ctrl+Alt+N
#
"""
學習物件導向
"""

action_list = {
    "add": AddStu, 
    "del": DelStu, 
    "modify": ModifyStu, 
    "show": PrintAll
}

def main():
    student_dict = StudentInfoProcessor().read_student_file()
    select_result = "initial"

    while select_result != "exit":
        select_result = print_menu()
        try:
            student_dict = action_list[select_result](student_dict).execute()
        except:
            pass
    
    StudentInfoProcessor().restore_student_file(student_dict)

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