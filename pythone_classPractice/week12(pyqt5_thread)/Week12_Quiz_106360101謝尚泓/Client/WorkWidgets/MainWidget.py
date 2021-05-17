from PyQt5 import QtWidgets, QtGui, QtCore
from WorkWidgets.AddStuWidget import AddStuWidget
from WorkWidgets.WorkWidgetComponents import LabelComponent


class MainWidget(QtWidgets.QWidget):
    def __init__(self, socket_client):
        super().__init__()
        self.socket_client = socket_client
        self.setObjectName("main_widget")

        layout = QtWidgets.QVBoxLayout() #水平layout
        header_label = LabelComponent(24, "Student Management System")
        add_stu_widget = AddStuWidget(self.socket_client)

        layout.addWidget(header_label, stretch=20)
        layout.addWidget(add_stu_widget, stretch=80)

        self.setLayout(layout)
