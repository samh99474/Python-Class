from SocketClient import SocketClient
from AddStu import AddStu
from PrintAll import PrintAll

action_list = {
    "add": AddStu, 
    "show": PrintAll
}

def main():
    client = SocketClient()
    select_result = "initial"

    while select_result != "exit":
        select_result = print_menu()
        try:
            action_list[select_result](client).execute()
        except:
            pass

    client.client_socket.close()

def print_menu():
    print()
    print("add: Add a student's name and score")
    print("show: Print all")
    print("exit: Exit")
    selection = input("Please select: ")

    return selection

main()