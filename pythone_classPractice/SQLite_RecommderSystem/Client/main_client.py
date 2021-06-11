from SocketClient.Socket_Client import SocketClient
from AddUser import AddUser
from Get_Movie_RS import Get_Movie_RS
from Rating import Rating

action_list = {
    "add": AddUser,
    "RS" : Get_Movie_RS,
    "rating": Rating
}

#======================================================================
def print_menu():
        print()
        print("add: Add a student's name")
        print("RS: Get Movie Recommemdation")
        print("rating: rating a Movie")
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