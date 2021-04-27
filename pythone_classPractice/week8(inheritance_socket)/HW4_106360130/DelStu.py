class DelStu :
    def __init__(self, student_list) :
        self.student_list = student_list

    def execute(self) :
        print("del_stu")
        name = input("  Please input a student's name: ")

        search_fail = True
        print("Here")
        for student_info in self.student_list :
            if student_info["name"] == name :
                self.student_list.remove(student_info)
                print("    Del {} success".format(name))
                search_fail = False

        if search_fail :
            print("  The name {} is not found".format(name))

        return self.student_list

"""
def main(student_list):
    print("del_stu")
    name = input("  Please input a student's name: ")

    search_fail = True
    for student_info in student_list :
        if student_info["name"] == name :
            student_list.remove(student_info)
            print("    Del {} success".format(name))
            search_fail = False

    if search_fail :
        print("  The name {} is not found".format(name))
"""



"""
student_list = [{'name': 'Leo', 'scores': {'math': 98.0, 'english': 87.0, 'chinese': 87.0}}, {'name': 'Jeff', 
'scores': {'math': 95.0, 'chinese': 54.0, 'english': 88.0}}]

print("Before : \n{}".format(student_list))
main(student_list)
print("After : \n{}".format(student_list))
"""














