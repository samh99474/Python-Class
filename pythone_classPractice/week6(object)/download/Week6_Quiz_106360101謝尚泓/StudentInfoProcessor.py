import pickle
class StudentInfoProcessor():

    def read_student_file(self):
        self.student_dict = dict()
        try:
            with open("student_list.txt", "rb") as fp:
                self.student_dict = pickle.load(fp)
        except:
            pass

        return self.student_dict

    def restore_student_file(self, student_dict):
        
        with open("student_list.txt", "wb") as fp:
            pickle.dump(student_dict, fp)
