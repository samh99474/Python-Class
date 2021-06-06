import tornado.websocket
import json
import socket



class Echo:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket.connect(("127.0.0.1", 10000))

    def execute(self, message):
        send_data = {'command': "echo", "parameter": message}
        self.client_socket.send(json.dumps(send_data).encode())


command_dict = {
    "echo": Echo
}


class WSHandler(tornado.websocket.WebSocketHandler):
    clients = []

    def check_origin(self, origin):
        return True

    def open(self):
        WSHandler.clients.append(self)

    def on_message(self, message):
        print ("The received message: {}".format(message))
        try:
            message = json.loads(message)
            command_dict[message['command']]().execute(message['parameter'])
        except Exception as e:
            print("errors {}: '{}'".format(e, message))
            self.write_to_clients(self.clients, "fail")

    def on_close(self):
        print("Client disconnected")
        WSHandler.clients.remove(self)

    def write_to_clients(self, clients, message):
        for client in clients:
            client.write_message(message)