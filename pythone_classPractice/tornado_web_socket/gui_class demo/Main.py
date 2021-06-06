from WorkWidgets.MainWidget import MainWidget
from SocketServer import SocketServer
from PyQt5.QtWidgets import QApplication
from PyQt5 import sip
import sys


server = SocketServer("127.0.0.1", 10000)
server.serve()

app = QApplication([])
main_window = MainWidget(server)

main_window.setFixedSize(500, 300)
main_window.show()


sys.exit(app.exec_())