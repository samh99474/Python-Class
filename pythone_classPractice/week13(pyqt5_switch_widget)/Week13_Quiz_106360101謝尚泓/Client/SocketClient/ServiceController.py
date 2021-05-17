from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSignal

import json

class ExecuteCommand(QtCore.QThread):
    return_sig = pyqtSignal(str)
    socket_client = None

    def __init__(self, command, dict_data):
        super().__init__()
        self.command = command
        self.dict_data = dict_data

    def run(self):
        #Send command and parameters(data) to the socket server
        self.socket_client.send_command(self.command, self.dict_data)
        print("\nclient send data to server => \'command\':{}, \'parameters\':{}".format(self.command, self.dict_data))

        #waiting for response from the socket server
        boolean, result = self.socket_client.wait_response()
        result = json.loads(result) # convert dictionary string to dictionary
        self.return_sig.emit(json.dumps(result))