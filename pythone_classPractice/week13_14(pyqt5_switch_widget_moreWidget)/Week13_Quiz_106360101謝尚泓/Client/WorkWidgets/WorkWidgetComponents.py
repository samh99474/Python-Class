from PyQt5 import QtWidgets, QtCore, QtGui


class LabelComponent(QtWidgets.QLabel):
    def __init__(self, font_size, content, color = "black"):
        super().__init__()

        self.setWordWrap(True)
        self.setAlignment(QtCore.Qt.AlignCenter)

        self.setFont(QtGui.QFont("微軟正黑體", font_size, QtGui.QFont.Bold))
        self.setText(content)

        self.setStyleSheet("color:"+color+";")
        #self.setStyleSheet("color: blue; background-color: yellow")


class LineEditComponent(QtWidgets.QLineEdit):
    def __init__(self, default_content="", length=10, width=200, font_size=16, Enable=True):
        super().__init__()
        self.setMaxLength(length)
        self.setText(default_content)
        self.setStyleSheet("color:black;")
        self.setMinimumHeight(30)
        self.setMaximumWidth(width)
        self.setFont(QtGui.QFont("微軟正黑體", font_size))
        self.setEnabled(Enable)


class ButtonComponent(QtWidgets.QPushButton):
    def __init__(self, text, font_size=16):
        super().__init__()
        self.setText(text)
        self.setFont(QtGui.QFont("微軟正黑體", font_size))
