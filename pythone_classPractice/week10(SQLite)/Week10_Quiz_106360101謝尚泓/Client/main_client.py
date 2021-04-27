from Socket_Client import SocketClient
from AddStu import AddStu
from ModifyStu import ModifyStu
from DelStu import DelStu
from PrintAll import PrintAll

host = "127.0.0.1"
port = 20001

action_list = {
    "add": AddStu,
    "modify": ModifyStu,
    "del": DelStu,
    "show": PrintAll
}

#======================================================================
def print_menu():
        print()
        print("add: Add a student's name and score")
        print("modify: Modify a student's score")
        print("del: Delete a student")
        print("show: Print all")
        print("exit: Exit")
        selection = input("Please select: ")

        return selection

#================================================================

def main():

    client = SocketClient(host, port)
    select_result = "initial"

    while select_result != "exit":
        select_result = print_menu()
        try:
            action_list[select_result](client).execute()
        except:
            pass

    client.client_socket.close()

main()