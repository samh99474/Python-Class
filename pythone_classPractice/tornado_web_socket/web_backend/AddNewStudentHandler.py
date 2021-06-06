import tornado.web


class AddNewStudentHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        stu_id = self.get_argument("stu_id")
        stu_name = self.get_argument("stu_name")

        print(stu_id, stu_name)

        ret_dict = {"status": "Okay"}
        self.write(ret_dict)
