"""
socket client端
打開client:
在VScode裡的terminal終端機打:python ./client_demo.py

如何結束?
在client terminal輸入"close"，傳送給server端(即可終止連線)
最後在server端cmd打"finish"
"""
import socket 
import json
BUFFER_SIZE = 1940

host = "127.0.0.1"
port = 20001

class SocketClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket.connect((host, port))
 
    def send_command(self, command, studentDic):
        send_data = {'command': command, 'parameters': studentDic}
        self.client_socket.send(json.dumps(send_data).encode())     #因為send_data是dict，所以要轉換成JSON格式才能傳送

    def wait_response(self):
        data = self.client_socket.recv(BUFFER_SIZE)
        raw_data = data.decode()
        print("client received the response data from server => {}".format(raw_data))

        if raw_data == "closing":
            return False, raw_data
        
        return True, raw_data
    

    