"""
socket server端
在cmd打:python server_demo.py
才能再client 端開啟連線

如何結束?
在client terminal輸入"close"，傳送給server端(即可終止連線)
最後在server端cmd打"finish"
"""
from threading import Thread
import socket
import json
import time
import pickle
from StudentInfoProcessor import StudentInfoProcessor
from PrintAll import PrintAll

host = "127.0.0.1"
port = 20001


class SocketServer(Thread):
    def __init__(self, host, port):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # This following setting is to avoid the server crash. So, the binded address can be reused
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)

    def serve(self):
        self.start()

    def run(self):
        while True:
            connection, address = self.server_socket.accept()
            print("{} connected".format(address))
            self.new_connection(connection=connection,
                                address=address)


    def new_connection(self, connection, address):
        try:
            Thread(target=self.receive_message_from_client,
                kwargs={
                    "connection": connection,
                    "address": address}, daemon=True).start()
        except: pass

    def receive_message_from_client(self, connection, address):
        keep_going = True
        while keep_going:
            try:
                message = connection.recv(1024).strip().decode()
            except:
                keep_going = False
            else:
                if not message:
                    break
                message = json.loads(message)

                if message['command'] == "close" or message['command']=="exit":
                    connection.send("closing".encode())
                    break
                else:
                    student_dict = StudentInfoProcessor().read_student_file()
                    #init
                    has_item = False
                    status = False

                    if message['command'] == "add":
                        try:
                            for student_dict_name, student_dict_info in student_dict.items():
                                for new_student_dict_name, new_student_dict_info in message['parameters'].items():  #message['parameters'] 是dict
                                    if(student_dict_name == new_student_dict_name): #已存在Name
                                        has_item = True
                                        status = False
                                        break   #student_dict.items()之info name 停止在輸入的name，才不會一直跑下去跑到錯誤(最後)的item
                                    else:
                                        student_dict.update(message['parameters'])
                                        has_item = False
                                        status = True

                            if(len(student_dict.items()) == 0):     #若原始dict為空，不會有已存在Name的問題，則可以將新data直接merge(update)加入
                                student_dict.update(message['parameters'])
                                has_item = False
                                status = True

                        except Exception as e:      #若try有錯誤，則執行except
                            print("The exception {} occurs.".format(e))
                        
                        if(status == True):
                            StudentInfoProcessor().restore_student_file(student_dict)
                            reply_msg = "server received the data from client => \'status\':{}, \'parameters\':{}".format(status, message['parameters'])
                        else:
                            reply_msg = "server received the data from client => \'status\':{}, \''reason'\': \'The name already exists.\'".format(status)

                    elif message['command'] == "show":
                        status = True
                        if(status == True):
                            reply_msg = "server received the data from client => \'status\':{}, \'parameters\':{}".format(status, student_dict)
                            reply_msg += PrintAll(student_dict).execute() #python 字串的append的方法
                        else:
                            reply_msg = "server received the data from client => \'status\':{}, \''reason'\': \'Fail to show.\'".format(status)

                    connection.send(reply_msg.encode())
                    
        
        connection.close()
        print("close connection")


if __name__ == '__main__':
    server = SocketServer(host, port)
    server.setDaemon(True)
    server.serve()

    # because we set daemon is true, so the main thread has to keep alive
    while True:
        command = input()
        if command == "finish":
            break
    
    server.server_socket.close()
    print("leaving ....... ")
