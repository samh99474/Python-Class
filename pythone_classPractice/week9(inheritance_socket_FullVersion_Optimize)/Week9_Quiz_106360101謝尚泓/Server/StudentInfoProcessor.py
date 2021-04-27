import pickle
class StudentInfoProcessor():
    """def __init__(self):
        # Nothing to init
"""
    def read_student_file(self):
        self.student_dict = dict()
        try:
            with open("student_list.txt", "rb") as fp:
                self.student_dict = pickle.load(fp)
        except Exception as e:  # 若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))

        return self.student_dict

    def restore_student_file(self, student_dict):
        try:
            with open("student_list.txt", "wb") as fp:
                pickle.dump(student_dict, fp)
        except Exception as e:  # 若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))
