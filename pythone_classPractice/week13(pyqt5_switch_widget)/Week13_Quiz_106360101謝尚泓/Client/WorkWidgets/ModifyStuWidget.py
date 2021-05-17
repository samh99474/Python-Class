from PyQt5 import QtWidgets
from WorkWidgets.WorkWidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
from SocketClient.ServiceController import ExecuteCommand

import time

import json

class ModifyStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.query_student_dict = dict()
        self.student_dict = dict()
        
        self.setObjectName("modify_stu_widget")

        layout = QtWidgets.QGridLayout()

        header_label = LabelComponent(20, "Modify Student")
        result_label = LabelComponent(20, "Result")
        self.result_content = LabelComponent(10, "請先查詢欲修改之學生", "blue")

        self.content_label_name = LabelComponent(16, "Name: ")
        self.editor_label_name = LineEditComponent("")  #input name

        self.content_label_subject = LabelComponent(16, "Subject: ")
        self.editor_label_subject = LineEditComponent("")   #input subject

        self.content_label_score = LabelComponent(16, "Score: ")
        self.editor_label_score = LineEditComponent("") #input score

        self.button_Query = ButtonComponent("Query")
        self.button_Modify = ButtonComponent("Modify")
        self.send_button = ButtonComponent("SEND MODIFY")

        
        layout.addWidget(header_label, 0, 0, 1, 2)  #(grid_x, grid_y, row佔幾格, column佔幾格)
        layout.addWidget(result_label, 0, 3, 1, 2)
        layout.addWidget(self.result_content, 1, 3, 2, 1)
        layout.addWidget(self.content_label_name, 1, 0, 1, 1)
        layout.addWidget(self.content_label_subject, 2, 0, 1, 1)
        layout.addWidget(self.content_label_score, 3, 0, 1, 1)
        layout.addWidget(self.editor_label_name, 1, 1, 1, 2)
        layout.addWidget(self.editor_label_subject, 2, 1, 1, 2)
        layout.addWidget(self.editor_label_score, 3, 1, 1, 2)
        layout.addWidget(self.button_Query, 1, 2, 1, 1)
        layout.addWidget(self.button_Modify, 3, 2, 1, 1)
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
        self.button_Modify.setEnabled(False)
        self.editor_label_subject.setEnabled(False)
        self.editor_label_score.setEnabled(False)
        self.send_button.setEnabled(False)
        self.button_Query.clicked.connect(self.Query_action)
        self.button_Modify.clicked.connect(self.Modify_action)
        self.send_button.clicked.connect(self.send_action)
    
    def Modify_action(self):
        scoreFormat_is_correct = False
        
        if( (len(self.editor_label_name.text()) != 0) and (len(self.editor_label_subject.text()) != 0) and (len(self.editor_label_score.text()) != 0)):
            try:
                self.score = int(self.editor_label_score.text())
                self.scoreFormat_is_correct = True
            except Exception as e:  # 若try有錯誤，則執行except
                self.scoreFormat_is_correct = False
                print("The exception {} occurs.".format(e))
            finally:
                if(self.scoreFormat_is_correct and self.score>=0):
                    if(self.editor_label_name.text() not in self.student_dict):
                        self.student_dict[self.editor_label_name.text()] = {}
                    
                    self.student_dict[self.editor_label_name.text()][self.editor_label_subject.text()] = self.editor_label_score.text()
                    self.result_content.setText("待傳送資料為:{}\n確認無誤後按下SEND".format(self.student_dict))
                    self.result_content.setStyleSheet("color:green;")
                    self.send_button.setEnabled(True)
                    
                else:
                    self.result_content.setText("成績不能為負數或字串")
                    self.result_content.setStyleSheet("color:red;")
        else:
            self.result_content.setText("資料不完整，請重新檢查並傳送")
            self.result_content.setStyleSheet("color:red;")
        print(self.editor_label_name.text())
        
            
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
        self.modify_toServer_action(self.student_dict)

    
    def reset(self):
        self.query_student_dict = {}
        self.student_dict = {}
        self.editor_label_name.clear()
        self.editor_label_subject.clear()
        self.editor_label_score.clear()
        
        self.button_Modify.setEnabled(False)
        self.editor_label_subject.setEnabled(False)
        self.editor_label_score.setEnabled(False)
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
            print("此名稱存在，您可以修改此學生")
            self.result_content.setText("已查詢{}成功，此名稱存在，您可以修改此學生, return_status:{}\n學生目前科目:{}".format(self.editor_label_name.text(), result['status'], result['parameters']))
            self.result_content.setStyleSheet("color:green;")
            self.editor_label_subject.setEnabled(True)
            self.editor_label_score.setEnabled(True)
            self.button_Modify.setEnabled(True)

        else:
            self.query_student_dict = {}
            self.student_dict = {}
            print("此名稱不存在，您不可以修改此學生")
            self.result_content.setText("已查詢{}成功，此名稱不存在，您不可以修改此學生".format(self.editor_label_name.text()))
            self.result_content.setStyleSheet("color:red;")
            self.editor_label_subject.setEnabled(False)
            self.editor_label_score.setEnabled(False)
            self.button_Modify.setEnabled(False)
            self.send_button.setEnabled(False)


    def modify_toServer_action(self, student_dict):
            self.send_command = ExecuteCommand(command = "modify", dict_data = self.student_dict)
            self.send_command.start()
            self.send_command.return_sig.connect(self.process_result_modify_toServer)
            return_status = self.process_result_modify_toServer

    def process_result_modify_toServer(self, result):
        result = json.loads(result)
        self.result_content.setText("status: {}".format(result['status']))
        if result['status'] == "OK":
            self.result_content.setText("已成功修改資料:{}\n".format(self.student_dict))
            self.result_content.setStyleSheet("color:green;")
            self.reset()
            print("    modify {} success".format(self.student_dict))
            print("修改成功")
        else:
            self.result_content.setText("修改資料失敗\n")
            self.result_content.setStyleSheet("color:red;")
            self.reset()
            print("    modify {} fail".format(self.student_dict))

    def load(self):
        print("load ModifyStuWidget")
        print("show widget")


