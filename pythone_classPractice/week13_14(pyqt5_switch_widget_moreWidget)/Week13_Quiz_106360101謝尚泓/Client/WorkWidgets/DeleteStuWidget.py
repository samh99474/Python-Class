from PyQt5 import QtWidgets
from PyQt5.QtCore import reset
from WorkWidgets.WorkWidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
from SocketClient.ServiceController import ExecuteCommand

import time

import json

class DeleteStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.query_student_dict = dict()
        self.student_dict = dict()
        
        self.setObjectName("delete_stu_widget")

        layout = QtWidgets.QGridLayout()

        header_label = LabelComponent(20, "Delete Student")
        result_label = LabelComponent(20, "Result")
        self.result_content = LabelComponent(10, "請先查詢欲刪除之學生", "blue")

        self.content_label_name = LabelComponent(16, "Name: ")
        self.editor_label_name = LineEditComponent("")  #input name

        self.send_button = ButtonComponent("SEND DELETE")
        self.button_Query = ButtonComponent("Query")
        

        layout.addWidget(header_label, 0, 0, 1, 2)  #(grid_x, grid_y, row佔幾格, column佔幾格)
        layout.addWidget(result_label, 0, 3, 1, 2)
        layout.addWidget(self.result_content, 1, 3, 2, 1)
        layout.addWidget(self.content_label_name, 1, 0, 1, 1)
        layout.addWidget(self.editor_label_name, 1, 1, 1, 2)
        layout.addWidget(self.button_Query, 1, 2, 1, 1)
        layout.addWidget(self.send_button, 4, 3, 1, 1)

        layout.setColumnStretch(0, 5)   # column 0 width stretch 50%
        layout.setColumnStretch(1, 8)   # column 1 width stretch 90%
        layout.setColumnStretch(2, 6)
        layout.setColumnStretch(3, 10)
        layout.setRowStretch(0, 1)      # row 0 width stretch 比例佔1
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 5)

        self.setLayout(layout)

        self.execute()

    def execute(self):
        print("execute")
        if(len(self.editor_label_name.text()) != 0):
            self.editor_label_name.mousePressEvent = self.clear_editor_label_name
        
        self.send_button.setEnabled(False)
        self.button_Query.clicked.connect(self.Query_action)
        self.send_button.clicked.connect(self.send_action)
        
            
    def clear_editor_label_name(self, event):
        self.editor_label_name.clear()

    def Query_action(self):
        if(len(self.editor_label_name.text()) != 0):
            self.query_student_dict[self.editor_label_name.text()] = {}
            
            self.query_toServer_action(self.query_student_dict)

        else:
          self.result_content.setText("未輸入學生名稱，請輸入後再試")
          self.result_content.setStyleSheet("color:red;")
        print(self.editor_label_name.text())
    
    def send_action(self):
        self.delete_toServer_action(self.student_dict)

    
    def reset(self):
        self.query_student_dict = {}
        self.student_dict = {}
        self.editor_label_name.clear()

        self.send_button.setEnabled(False)

    def query_toServer_action(self, query_student_dict):
            self.send_command = ExecuteCommand(command = "query", dict_data = self.query_student_dict)
            self.send_command.start()
            self.send_command.return_sig.connect(self.process_result_query_toServer)
            return_status = self.process_result_query_toServer

    def process_result_query_toServer(self, result):
        result = json.loads(result)
        self.result_content.setText("status: {}".format(result['status']))
        if result['status'] == "OK":
            self.query_student_dict = {}
            self.student_dict = {}
            self.student_dict[self.editor_label_name.text()] = {}
            print("此名稱存在，您可以刪除此學生")
            self.result_content.setText("已查詢{}成功，此名稱存在，您可以刪除此學生，若確定刪除請按下SEND鍵, return_status:{}".format(self.editor_label_name.text(), result['status']))
            self.result_content.setStyleSheet("color:green;")
            self.send_button.setEnabled(True)

        else:
            self.query_student_dict = {}
            self.student_dict = {}
            print("此名稱不存在，您不可以刪除此學生")
            self.result_content.setText("已查詢{}成功，此名稱不存在，您不可以刪除此學生".format(self.editor_label_name.text()))
            self.result_content.setStyleSheet("color:red;")

    def delete_toServer_action(self, student_dict):
            self.send_command = ExecuteCommand(command = "del", dict_data = self.student_dict)
            self.send_command.start()
            self.send_command.return_sig.connect(self.process_result_delete_toServer)
            return_status = self.process_result_delete_toServer

    def process_result_delete_toServer(self, result):
        result = json.loads(result)
        self.result_content.setText("status: {}".format(result['status']))
        if result['status'] == "OK":
            self.result_content.setText("已成功刪除資料:{}\n".format(self.student_dict))
            self.result_content.setStyleSheet("color:green;")
            self.reset()
            print("    Delete {} success".format(self.student_dict))
            print("刪除成功")
        else:
            self.result_content.setText("刪除資料失敗\n")
            self.result_content.setStyleSheet("color:red;")
            self.reset()
            print("    Delete {} fail".format(self.student_dict))

    def load(self):
        self.reset()
        print("load DeleteStuWidget")
        print("show widget")


