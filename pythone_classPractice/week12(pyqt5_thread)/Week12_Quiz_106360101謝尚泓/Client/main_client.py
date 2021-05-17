from SocketClient.Socket_Client import SocketClient
from AddStu import AddStu
from ModifyStu import ModifyStu
from DelStu import DelStu
from PrintAll import PrintAll

from WorkWidgets.MainWidget import MainWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import sip
import sys


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
    
    client = SocketClient()

    app = QApplication([])
    main_window = MainWidget(client)

    main_window.setFixedSize(800, 400)
    main_window.show()
    # main_window.showFullScreen()

    select_result = "initial"

    sys.exit(app.exec_())
    client.client_socket.close()

main()