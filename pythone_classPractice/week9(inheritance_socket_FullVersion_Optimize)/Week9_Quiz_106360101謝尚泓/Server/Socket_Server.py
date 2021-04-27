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

class SocketServer(Thread):
    def __init__(self, host, port, Job_Dispatcher):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # This following setting is to avoid the server crash. So, the binded address can be reused
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)

        self.Job_Dispatcher = Job_Dispatcher

    def serve(self):
        self.start()    #start後，會自動執行run

    def run(self):
        try:
            while True:
                connection, address = self.server_socket.accept()
                print("{} connected".format(address))
                self.new_connection(connection=connection,
                                    address=address)
        except: pass

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
                    reply_msg = self.Job_Dispatcher.execute(message['command'], message['parameters'])

                    connection.send(json.dumps(reply_msg).encode())
        
        connection.close()
        print("close connection")





