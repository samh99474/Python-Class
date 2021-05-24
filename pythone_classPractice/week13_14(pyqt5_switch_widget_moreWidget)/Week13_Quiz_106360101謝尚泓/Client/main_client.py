from SocketClient.Socket_Client import SocketClient
from SocketClient.ServiceController import ExecuteCommand

from WorkWidgets.MainWidget import MainWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import sip
import sys

def main():
    
    ExecuteCommand.socket_client = SocketClient()

    app = QApplication([])
    main_window = MainWidget()

    main_window.setFixedSize(1000, 600)
    main_window.show()
    # main_window.showFullScreen()

    select_result = "initial"

    sys.exit(app.exec_())
    client.client_socket.close()

main()