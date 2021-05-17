"""
參考網站:
1.scrollbar
https://stackoverflow.com/questions/9624281/how-to-associate-a-horizontal-scrollbar-to-multiple-groupbox
"""
from PyQt5 import QtWidgets, QtGui, QtCore
from WorkWidgets.WorkWidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
from SocketClient.ServiceController import ExecuteCommand
import json

class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("show_stu_widget")

        layout = QtWidgets.QVBoxLayout()

        header_label = LabelComponent(20, "Show Student")

        self.result_content = LabelComponent(10, "結果顯示", "blue")

        scrolllayout = QtWidgets.QVBoxLayout()

        scrollwidget = QtWidgets.QWidget()
        scrollwidget.setLayout(scrolllayout)

        scroll = QtWidgets.QScrollArea()
        scroll.setWidgetResizable(True)  # Set to make the inner widget resize with scroll area
        scroll.setWidget(scrollwidget)

        scrolllayout.addWidget(self.result_content)

        layout.addWidget(header_label, stretch=1)
        layout.addWidget(scroll, stretch=1)
        self.setLayout(layout)

    def show_toServer_action(self):
            self.send_command = ExecuteCommand(command = "show", dict_data = dict())
            self.send_command.start()
            self.send_command.return_sig.connect(self.process_result_show_toServer)
            return_status = self.process_result_show_toServer

    def process_result_show_toServer(self, result):
        result = json.loads(result)
        self.result_content.setText("status: {}".format(result['status']))

        if result['status'] == "OK":
            student_dict = result['parameters']
            
            PrintAll_studentList = "\n==== student list ====\n"
            for student_dict_name, student_dict_info in student_dict.items():
                PrintAll_studentList += "\n\nName: " + student_dict_name
                for key in student_dict_info:
                    PrintAll_studentList += "   subject:" + str(key) + "\'score\':" + str(student_dict_info[key])
            PrintAll_studentList += "\n======================"

            self.result_content.setText("成功讀取所有學生資料:\nstatus: {}\n\n所有學生資料: \n{}".format(result['status'], PrintAll_studentList))
            self.result_content.setStyleSheet("color:green;")
            print("    show success")
        else:
            self.result_content.setText("資料讀取失敗\n")
            self.result_content.setStyleSheet("color:red;")
            print("    show fail")
        
    def load(self):
        self.show_toServer_action()
        print("load showStuWidget")
        print("show widget")
