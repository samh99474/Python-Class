import pickle

class StudentInfoProcessor :

    def read_student_file(self):
        self.student_list = list()
        try:
            with open("student_list.txt", "rb") as fp:
                self.student_list = pickle.load(fp)
        except:
            pass

        return self.student_list

    def restore_student_file(self, student_list):

        with open("student_list.txt", "wb") as fp:
            pickle.dump(student_list, fp)
