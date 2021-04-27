class PrintAll():
    def __init__(self, student_dict):
        self.student_dict = student_dict

    def execute(self):
        try:
            PrintAll_studentList = "\n==== student list ====\n"
            for student_dict_name, student_dict_info in self.student_dict.items():
                PrintAll_studentList += "\nName: " + student_dict_name
                for key in student_dict_info:
                    PrintAll_studentList += "   subject:" + str(key) + "\'score\':" + str(student_dict_info[key])
            PrintAll_studentList += "\n======================"
            
        except Exception as e:      #若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))
        finally:
            return PrintAll_studentList

"""student_dict = {'kelly': {'english': 60, 'chinese': 90},
          'apple': {'english': 62, 'chinese': 80}}
x = PrintAll(student_dict).execute()
print(x)"""
                
