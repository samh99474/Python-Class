from ServerAction.Server_QueryStu import Server_QueryStu
from ServerAction.Server_AddStu import Server_AddStu
from ServerAction.Server_ModifyStu import Server_ModifyStu
from ServerAction.Server_DelStu import Server_DelStu
from ServerAction.Server_PrintAll import Server_PrintAll

from Socket_Server import SocketServer

from DB.DBConnection import DBConnection
from DB.DBInitializer import DBInitializer

host = "127.0.0.1"
port = 20001

action_list = {
    "query": Server_QueryStu,
    "add": Server_AddStu,
    "modify": Server_ModifyStu,
    "del": Server_DelStu,
    "show": Server_PrintAll
}
class JobDispatcher:
    def __init__(self):
        DBConnection.db_file_path = "example.db"
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