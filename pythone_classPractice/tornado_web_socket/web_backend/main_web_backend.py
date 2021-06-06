from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import tornado.web
import tornado.websocket
from IndexHandler import IndexHandler
from AddNewStudentHandler import AddNewStudentHandler
from WSHandler import WSHandler


class WebBackend:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start_serving(self):
        app = self.init_server_application()
        server = HTTPServer(app)
        server.listen(port=self.port, address=self.host)
        IOLoop.current().start()

    def init_server_application(self):  #Route
        return tornado.web.Application(
            [
                (r"/", IndexHandler),
                (r"/add_student", AddNewStudentHandler),
                (r"/web_socket", WSHandler)
            ]
        )


WebBackend(host="127.0.0.1", port=9000).start_serving()
