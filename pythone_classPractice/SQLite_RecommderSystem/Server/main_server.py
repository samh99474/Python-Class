from ServerAction.Server_Get_Movie_RS import Server_Get_Movie_RS
from ServerAction.Server_AddUser import Server_AddUser
from ServerAction.Server_QueryUser import Server_QueryUser
from ServerAction.Server_Rating import Server_Rating

from Socket_Server import SocketServer

from DB.DBConnection import DBConnection
from DB.DBInitializer import DBInitializer

host = "127.0.0.1"
port = 20001

action_list = {
    "RS": Server_Get_Movie_RS,
    "queryUser": Server_QueryUser,
    "addUser": Server_AddUser,
    "rating": Server_Rating
}
class JobDispatcher:
    def __init__(self):
        DBConnection.db_file_path = "./UserMovie.db"
        DBInitializer().execute()

    def execute(self, command, parameters):
        reply_msg = action_list[command]().execute(parameters)
        return reply_msg


def open_server(host, port):
    Job_Dispatcher = JobDispatcher()
    server = SocketServer(host, port, Job_Dispatcher)
    server.setDaemon(True)
    server.serve()
    print("Server Open")

    # because we set daemon is true, so the main thread has to keep alive
    while True:
        command = input()
        if command == "finish":
            break
    
    server.server_socket.close()
    print("leaving ....... ")

def main():
    open_server(host, port)

main()