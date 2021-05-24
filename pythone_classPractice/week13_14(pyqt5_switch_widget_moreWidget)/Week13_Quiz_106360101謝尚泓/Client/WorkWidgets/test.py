
from PyQt5 import QtWidgets, QtGui, QtCore
from WorkWidgetComponents import LabelComponent, LineEditComponent, ButtonComponent

import time


class ModifyStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("modify_stu_widget")

        layout = QtWidgets.QVBoxLayout()

        header_label = LabelComponent(20, "Modify Student")
        modify_widget = ModifyWidget()

        layout.addWidget(header_label, stretch=1)
        layout.addWidget(modify_widget, stretch=8)
        self.setLayout(layout)
    
    def load(self):
        print("modify widget")


class ModifyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("modify_stu_widget")

        layout = QtWidgets.QVBoxLayout()

        self.radio_button_change = QtWidgets.QRadioButton('Change')
        self.radio_button_add = QtWidgets.QRadioButton('Add new')

        self.radio_button_change.toggled.connect(self.radio_button_on_clicked)
        self.radio_button_add.toggled.connect(self.radio_button_on_clicked)


        self.combo_box_score = QtWidgets.QComboBox()
        self.combo_box_score.addItems(["Math", "English"])
        self.combo_box_score.currentIndexChanged.connect(self.combo_box_select_changed)


        layout.addWidget(self.radio_button_change)
        layout.addWidget(self.radio_button_add)
        layout.addWidget(self.combo_box_score)

        self.setLayout(layout)

    def radio_button_on_clicked(self):
        selected_button = self.sender()
        if selected_button.isChecked():
            print("{}".format(selected_button.text()))


    def combo_box_select_changed(self, index):
        print ("Index {} {} selected".format(index, self.combo_box_score.currentText()))

