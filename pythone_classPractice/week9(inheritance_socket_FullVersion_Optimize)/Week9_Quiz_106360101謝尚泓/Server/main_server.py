from Socket_Server import SocketServer
from Server_QueryStu import Server_QueryStu
from Server_AddStu import Server_AddStu
from Server_ModifyStu import Server_ModifyStu
from Server_DelStu import Server_DelStu
from Server_PrintAll import Server_PrintAll
from StudentInfoProcessor import StudentInfoProcessor

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
        self.student_dict = StudentInfoProcessor().read_student_file()

    def execute(self, command, parameters):
        self.student_dict, reply_msg = action_list[command](self.student_dict).execute(parameters)
        return reply_msg
    def job_finish(self):
        StudentInfoProcessor().restore_student_file(self.student_dict)


def open_server(host, port):
    Job_Dispatcher = JobDispatcher()
    server = SocketServer(host, port, Job_Dispatcher)
    server.setDaemon(True)
    server.serve()

    # because we set daemon is true, so the main thread has to keep alive
    while True:
        command = input()
        if command == "finish":
            break
    
    server.server_socket.close()
    Job_Dispatcher.job_finish() #close 最後存檔
    print("leaving ....... ")

def main():
    open_server(host, port)

main()