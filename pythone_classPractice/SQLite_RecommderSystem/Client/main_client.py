from SocketClient.Socket_Client import SocketClient
from AddUser import AddUser
from Get_Movie_RS import Get_Movie_RS

action_list = {
    "add": AddUser,
    "RS" : Get_Movie_RS

}

#======================================================================
def print_menu():
        print()
        print("add: Add a student's name")
        print("RS: Get Movie Recommemdation")
        print("exit: Exit")
        selection = input("Please select: ")

        return selection

#================================================================

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

main()