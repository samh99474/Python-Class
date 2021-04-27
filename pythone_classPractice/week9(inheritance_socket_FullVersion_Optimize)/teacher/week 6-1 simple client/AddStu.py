class AddStu:
    def __init__(self, socket_client):
        self.socket_client = socket_client

    def execute(self):
        name = input("  Please input a student's name: ")
        score_dict = dict()

        while True:
            subject = input("  Please input a subject name or exit for ending: ")
            if subject != "exit":
                while True:
                    try:
                        score = float(input("  Please input {}'s {} score or < 0 for discarding the subject: ".format(name, subject)))
                    except Exception as e:
                        print ("    Wrong format with reason {}, try again".format(e))
                    else:
                        if score > 0.0:
                            score_dict[subject] = score
                        break
            else:
                break

        if len(score_dict) > 0:
            basic_info ={
                "name": name,
                "scores": score_dict
            }

            self.socket_client.send_command("add", basic_info)
            result = self.socket_client.wait_response()

            if result['status'] == "OK":
                print("    Add {} success".format(basic_info))
            else:
                print("    Add {} fail".format(basic_info))
        else:
            print("    Add nothing")
