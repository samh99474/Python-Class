class PrintAll():
    def __init__(self, student_dict):
        self.student_dict = student_dict

    def execute(self):
        try:
            print ("\n==== student list ====\n")
            for student_dict_name, student_dict_info in self.student_dict.items():
                print("Name: ", student_dict_name)
                for key in student_dict_info:
                    print("   subject:"+ key + ', score: ', student_dict_info[key])
            print ("======================")
            
        except Exception as e:      #若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))
        finally:
            return self.student_dict
