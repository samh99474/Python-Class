from PyQt5 import QtWidgets, QtGui, QtCore
from WorkWidgetComponents import LabelComponent, LineEditComponent, ButtonComponent


class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("add_stu_widget")

        layout = QtWidgets.QGridLayout()

        header_label = LabelComponent(20, "Add Student")
        result_label = LabelComponent(20, "Result")
        result_content = LabelComponent(10, "Result_content...", "blue")

        content_label_name = LabelComponent(16, "Name: ")
        self.editor_label_name = LineEditComponent("input name")
        self.editor_label_name.mousePressEvent = self.clear_editor_content

        content_label_subject = LabelComponent(16, "Subject: ")
        self.editor_label_subject = LineEditComponent("input subject")
        self.editor_label_subject.mousePressEvent = self.clear_editor_content

        content_label_score = LabelComponent(16, "Score: ")
        self.editor_label_score = LineEditComponent("input score")
        self.editor_label_score.mousePressEvent = self.clear_editor_content

        button_Query = ButtonComponent("Query")
        button_Query.clicked.connect(self.Query_action)

        button_Add = ButtonComponent("Add")
        button_Add.clicked.connect(self.Add_action)

        send_button = ButtonComponent("SEND")
        send_button.clicked.connect(self.send_action)

        layout.addWidget(header_label, 0, 0, 1, 2)  #(grid_x, grid_y, row佔幾格, column佔幾格)
        layout.addWidget(result_label, 0, 3, 1, 2)
        layout.addWidget(result_content, 2, 3, 2, 1)
        layout.addWidget(content_label_name, 1, 0, 1, 1)
        layout.addWidget(content_label_subject, 2, 0, 1, 1)
        layout.addWidget(content_label_score, 3, 0, 1, 1)
        layout.addWidget(self.editor_label_name, 1, 1, 1, 2)
        layout.addWidget(self.editor_label_subject, 2, 1, 1, 2)
        layout.addWidget(self.editor_label_score, 3, 1, 1, 2)
        layout.addWidget(button_Query, 1, 2, 1, 1)
        layout.addWidget(button_Add, 3, 2, 1, 1)
        layout.addWidget(send_button, 4, 3, 1, 1)

        layout.setColumnStretch(0, 5)   # column 0 width stretch 50%
        layout.setColumnStretch(1, 8)   # column 1 width stretch 90%
        layout.setColumnStretch(2, 6)
        layout.setColumnStretch(3, 5)
        layout.setRowStretch(0, 1)      # row 0 width stretch 比例佔1
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 5)

        self.setLayout(layout)

    def clear_editor_content(self, event):
        self.editor_label_name.clear()
        self.editor_label_subject.clear()
        self.editor_label_score.clear()

    def Query_action(self):
        print(self.editor_label_name.text())
    def Add_action(self):
        print(self.editor_label_name.text())
    
    def send_action(self):
        print(self.editor_label_name.text())