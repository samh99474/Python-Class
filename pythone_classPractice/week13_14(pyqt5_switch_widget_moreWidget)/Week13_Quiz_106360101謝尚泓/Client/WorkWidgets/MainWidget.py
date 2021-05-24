from PyQt5 import QtWidgets, QtGui, QtCore
from WorkWidgets.AddStuWidget import AddStuWidget
from WorkWidgets.ShowStuWidget import ShowStuWidget
from WorkWidgets.DeleteStuWidget import DeleteStuWidget
from WorkWidgets.ModifyStuWidget import ModifyStuWidget
from WorkWidgets.WorkWidgetComponents import LabelComponent, ButtonComponent

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("main_widget")

        layout = QtWidgets.QGridLayout()
        header_label = LabelComponent(24, "Student Management System")
        
        function_widget = FunctionWidget()
        menu_widget = MenuWidget(function_widget.update_widget)

        layout.addWidget(header_label, 0, 0, 1, 2)
        layout.addWidget(menu_widget, 1, 0, 1, 1)
        layout.addWidget(function_widget, 1, 1, 1, 1)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 6)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 6)

        self.setLayout(layout)

class MenuWidget(QtWidgets.QWidget):
    def __init__(self, update_widget_callback):
        super().__init__()
        self.setObjectName("menu_widget")
        self.update_widget_callback = update_widget_callback

        layout = QtWidgets.QVBoxLayout()
        add_button = ButtonComponent("Add student")
        show_button = ButtonComponent("Show all")
        delete_button = ButtonComponent("delete student")
        modify_button = ButtonComponent("modify student")
        add_button.clicked.connect(lambda: self.update_widget_callback("add")) #because we have the input argument, we need to use lambda 
        show_button.clicked.connect(lambda: self.update_widget_callback("show"))
        delete_button.clicked.connect(lambda: self.update_widget_callback("delete"))
        modify_button.clicked.connect(lambda: self.update_widget_callback("modify"))

        layout.addWidget(add_button, stretch=1)
        layout.addWidget(show_button, stretch=1)
        layout.addWidget(delete_button, stretch=1)
        layout.addWidget(modify_button, stretch=1)

        self.setLayout(layout)


class FunctionWidget(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        self.widget_dict = {
            "add": self.addWidget(AddStuWidget()),
            "delete": self.addWidget(DeleteStuWidget()),
            "modify": self.addWidget(ModifyStuWidget()),
            "show": self.addWidget(ShowStuWidget())
        }
        self.update_widget("add")
    
    def update_widget(self, name):
        self.setCurrentIndex(self.widget_dict[name])
        current_widget = self.currentWidget()
        current_widget.load()

