from PyQt5 import QtWidgets, QtGui, QtCore
from WorkWidgetComponents import LabelComponent


class MainWidget(QtWidgets.QWidget):
    def __init__(self, socket):
        super().__init__()
        socket.return_sig.connect(self.change_text)

        self.setObjectName("main_widget")

        layout = QtWidgets.QVBoxLayout()
        self.header_label = LabelComponent(24, "Student Management System")

        layout.addWidget(self.header_label, stretch=20)

        self.setLayout(layout)


    def change_text(self, message):
        self.header_label.setText(message)
