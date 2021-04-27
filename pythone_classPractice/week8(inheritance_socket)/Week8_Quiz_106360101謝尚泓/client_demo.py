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
from AddStu import AddStu


host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940


class SocketClient:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket.connect((host, port))
 
    def send_command(self, command, studentDic):
        send_data = {'command': command, 'parameters': studentDic}
        self.client_socket.send(json.dumps(send_data).encode())     #因為send_data是dict，所以要轉換成JSON格式才能傳送

    def wait_response(self):
        data = self.client_socket.recv(BUFFER_SIZE)
        raw_data = data.decode()
        print(raw_data)

        if raw_data == "closing":
            return False, raw_data
        
        return True, raw_data
#======================================================================
def print_menu():
        print()
        print("add: Add a student's name and score")
        print("show: Print all")
        print("exit: Exit")
        selection = input("Please select: ")

        return selection
def select_menu():
    select_result = "initial"
    student_dict = dict()
    action_list = {
        "add": AddStu, 
        #"show": PrintAll
    }
    
    while select_result != "exit":
            select_result = print_menu()
            try:
                student_dict = action_list[select_result](student_dict).execute()
            except:
                pass
            return select_result, student_dict
    return select_result, student_dict
#======================================================================

if __name__ == '__main__':
    client = SocketClient(host, port)

    keep_going = True
    while keep_going:
        
        command, studentDic = select_menu()
        print("\nclient send data to server => \'command\':{}, \'parameters\':{}".format(command, studentDic))
        #command = input("command >>>")
        #studentDic = {'ss':"22"}
        client.send_command(command, studentDic)

        keep_going, receive_studentData = client.wait_response()
        print("\nclient receive data that server response(server have recieved) : "+ receive_studentData)
    