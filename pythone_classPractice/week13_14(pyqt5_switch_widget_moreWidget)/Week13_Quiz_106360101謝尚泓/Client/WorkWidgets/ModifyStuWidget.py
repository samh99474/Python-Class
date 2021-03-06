from PyQt5 import QtWidgets
from PyQt5.QtCore import reset
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

        self.radio_button_change = QtWidgets.QRadioButton('Change the score of current subject')
        self.modify_content_label_subject = LabelComponent(16, "Subject: ")
        self.combo_box_subject = QtWidgets.QComboBox()
        self.combo_box_subject.currentIndexChanged.connect(self.combo_box_select_changed)
        self.modify_content_label_score = LabelComponent(16, "Score: ")
        self.modify_editor_label_score = LineEditComponent("") #input score


        self.radio_button_add = QtWidgets.QRadioButton('Add new subject')

        self.add_content_label_subject = LabelComponent(16, "Subject: ")
        self.add_editor_label_subject = LineEditComponent("")   #input subject

        self.add_content_label_score = LabelComponent(16, "Score: ")
        self.add_editor_label_score = LineEditComponent("") #input score

        self.button_Query = ButtonComponent("Query")
        self.button_Modify = ButtonComponent("Modify")
        self.button_AddNew = ButtonComponent("Add")
        self.send_button = ButtonComponent("SEND MODIFY")

        
        layout.addWidget(header_label, 0, 0, 1, 2)  #(grid_x, grid_y, row佔幾格, column佔幾格)
        layout.addWidget(result_label, 0, 3, 1, 2)
        layout.addWidget(self.result_content, 2, 3, 3, 1)

        layout.addWidget(self.content_label_name, 1, 0, 1, 1)
        layout.addWidget(self.editor_label_name, 1, 1, 1, 2)

        layout.addWidget(self.radio_button_change, 2, 0, 1, 2)
        layout.addWidget(self.modify_content_label_subject, 3, 0, 1, 1)
        layout.addWidget(self.combo_box_subject, 3, 1, 1, 1)
        layout.addWidget(self.modify_content_label_score, 4, 0, 1, 1)
        layout.addWidget(self.modify_editor_label_score, 4, 1, 1, 2)

        layout.addWidget(self.radio_button_add, 5, 0, 1, 2)
        layout.addWidget(self.add_content_label_subject, 6, 0, 1, 1)
        layout.addWidget(self.add_editor_label_subject, 6, 1, 1, 2)
        layout.addWidget(self.add_content_label_score, 7, 0, 1, 1)
        layout.addWidget(self.add_editor_label_score, 7, 1, 1, 2)

        layout.addWidget(self.button_Query, 1, 2, 1, 1)
        layout.addWidget(self.button_Modify, 4, 2, 1, 1)
        layout.addWidget(self.button_AddNew, 7, 2, 1, 1)
        layout.addWidget(self.send_button, 8, 3, 1, 1)

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
        self.radio_button_change.setEnabled(False)
        self.button_Modify.setEnabled(False)
        self.combo_box_subject.setEnabled(False)
        self.modify_editor_label_score.setEnabled(False)
        self.radio_button_add.setEnabled(False)
        self.button_AddNew.setEnabled(False)
        self.add_editor_label_subject.setEnabled(False)
        self.add_editor_label_score.setEnabled(False)
        self.send_button.setEnabled(False)

        self.radio_button_change.toggled.connect(self.modify_radio_button_on_clicked)
        self.radio_button_add.toggled.connect(self.add_radio_button_on_clicked)

        self.button_Query.clicked.connect(self.Query_action)
        self.button_Modify.clicked.connect(self.Modify_action)
        self.button_AddNew.clicked.connect(self.Add_action)

        self.send_button.clicked.connect(self.send_action)
    
    def Modify_action(self):
        scoreFormat_is_correct = False
        
        if( (len(self.editor_label_name.text()) != 0) and (len(self.combo_box_subject.currentText()) != 0) and (len(self.modify_editor_label_score.text()) != 0)):
            try:
                self.score = int(self.modify_editor_label_score.text())
                self.scoreFormat_is_correct = True
            except Exception as e:  # 若try有錯誤，則執行except
                self.scoreFormat_is_correct = False
                print("The exception {} occurs.".format(e))
            finally:
                if(self.scoreFormat_is_correct and self.score>=0):
                    if(self.editor_label_name.text() not in self.student_dict):
                        self.student_dict[self.editor_label_name.text()] = {}
                    
                    self.student_dict[self.editor_label_name.text()][self.combo_box_subject.currentText()] = self.modify_editor_label_score.text()
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

    def Add_action(self):
        scoreFormat_is_correct = False
        
        if( (len(self.editor_label_name.text()) != 0) and (len(self.add_editor_label_subject.text()) != 0) and (len(self.add_editor_label_score.text()) != 0)):
            try:
                self.score = int(self.add_editor_label_score.text())
                self.scoreFormat_is_correct = True
            except Exception as e:  # 若try有錯誤，則執行except
                self.scoreFormat_is_correct = False
                print("The exception {} occurs.".format(e))
            finally:
                if(self.scoreFormat_is_correct and self.score>=0):
                    if(self.editor_label_name.text() not in self.student_dict):
                        self.student_dict[self.editor_label_name.text()] = {}
                    
                    self.student_dict[self.editor_label_name.text()][self.add_editor_label_subject.text()] = self.add_editor_label_score.text()
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
        self.combo_box_subject.clear()
        self.modify_editor_label_score.clear()
        self.add_editor_label_subject.clear()
        self.add_editor_label_score.clear()
        
        self.radio_button_change.setEnabled(False)
        self.radio_button_add.setEnabled(False)
        self.combo_box_subject.setEnabled(False)
        self.modify_editor_label_score.setEnabled(False)
        self.button_Modify.setEnabled(False)
        self.button_AddNew.setEnabled(False)
        self.add_editor_label_subject.setEnabled(False)
        self.send_button.setEnabled(False)

    def query_toServer_action(self, query_student_dict):
            self.send_command = ExecuteCommand(command = "query", dict_data = self.query_student_dict)
            self.send_command.start()
            self.send_command.return_sig.connect(self.process_result_query_toServer)
            return_status = self.process_result_query_toServer

    def process_result_query_toServer(self, result):
        self.combo_box_subject.clear()
        result = json.loads(result)
        self.result_content.setText("status: {}".format(result['status']))
        if result['status'] == "OK":
            self.query_student_dict = {}
            self.student_dict = {}
            self.student_dict[self.editor_label_name.text()] = {}
            print("此名稱存在，您可以修改此學生")
            self.result_content.setText("已查詢{}成功，此名稱存在，您可以修改此學生, return_status:{}\n學生目前科目:{}".format(self.editor_label_name.text(), result['status'], result['parameters']))

            parameters = result['parameters']
            
            PrintAll_studentList = "\n==== student list ====\n"
            for student_dict_name, student_dict_info in parameters.items():
                PrintAll_studentList += "\n\nName: " + student_dict_name
                for key in student_dict_info:
                    PrintAll_studentList += "   subject:" + str(key) + "\'score\':" + str(student_dict_info[key])

            self.combo_box_subject.addItems(parameters[self.editor_label_name.text()])

            self.result_content.setStyleSheet("color:green;")
            self.combo_box_subject.setEnabled(True)
            self.modify_editor_label_score.setEnabled(True)
            self.radio_button_change.setEnabled(True)
            self.radio_button_change.setChecked(True)
            self.radio_button_add.setEnabled(True)
            self.button_Modify.setEnabled(True)

        else:
            self.query_student_dict = {}
            self.student_dict = {}
            print("此名稱不存在，您不可以修改此學生")
            self.result_content.setText("已查詢{}成功，此名稱不存在，您不可以修改此學生".format(self.editor_label_name.text()))
            self.result_content.setStyleSheet("color:red;")
            self.radio_button_change.setEnabled(False)
            self.combo_box_subject.setEnabled(False)
            self.modify_editor_label_score.setEnabled(False)
            self.add_editor_label_score.setEnabled(False)
            self.button_Modify.setEnabled(False)
            self.radio_button_add.setEnabled(False)
            self.add_editor_label_subject.setEnabled(False)
            self.add_editor_label_subject.setEnabled(False)
            self.button_AddNew.setEnabled(False)
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
    
    def modify_radio_button_on_clicked(self):
        selected_button = self.sender()
        if selected_button.isChecked():
            print("{}".format(selected_button.text()))

        self.combo_box_subject.setEnabled(True)
        self.modify_editor_label_score.setEnabled(True)
        self.button_Modify.setEnabled(True)

        self.button_AddNew.setEnabled(False)
        self.add_editor_label_subject.setEnabled(False)
        self.add_editor_label_score.setEnabled(False)

    def add_radio_button_on_clicked(self):
        selected_button = self.sender()
        if selected_button.isChecked():
            print("{}".format(selected_button.text()))
            
        self.combo_box_subject.setEnabled(False)
        self.modify_editor_label_score.setEnabled(False)
        self.button_Modify.setEnabled(False)

        self.button_AddNew.setEnabled(True)
        self.add_editor_label_subject.setEnabled(True)
        self.add_editor_label_score.setEnabled(True)

    def combo_box_select_changed(self, index):
        print ("Index {} {} selected".format(index, self.combo_box_subject.currentText()))


    def load(self):
        self.reset()
        print("load ModifyStuWidget")
        print("show widget")


