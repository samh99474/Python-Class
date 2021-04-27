class PrintAll:
    def __init__(self, socket_client):
        self.socket_client = socket_client

    def execute(self):
        self.socket_client.send_command("show", dict())
        result = self.socket_client.wait_response()

        if result['status'] == "OK":
            student_list = result['parameters']
            print ("\n==== student list ====\n")
            for student in student_list:
                print("Name: {}".format(student['name']))
                for subject, score in student['scores'].items():
                    print("  subject: {}, score: {}".format(subject, score))
                print()
            
            print ("======================")
        else:
            print("    Retrieve data fail")
