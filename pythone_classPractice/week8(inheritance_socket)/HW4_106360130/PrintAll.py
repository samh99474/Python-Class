class PrintAll :
    def __init__(self, student_list):
        self.student_list = student_list

    def execute(self) :
        print ("\n==== student list ====")
        print("Here")
        for student_info in self.student_list :
            #print("student_info : \n{}".format(student_info))
            print("\nName: {}".format(student_info["name"]))
            for subject in student_info["scores"] :
                scores = student_info["scores"]
                #print(type(subject))  #"str"
                print("  subject: {}, score: {}".format(subject, scores[subject]))
                #print(score.keys())

        print ("\n======================")

        return self.student_list



"""
def main(student_list):
    print ("\n==== student list ====")

    for student_info in student_list :
        #print("student_info : \n{}".format(student_info))
        print("\nName: {}".format(student_info["name"]))
        for subject in student_info["scores"] :
            scores = student_info["scores"]
            #print(type(subject))  #"str"
            print("  subject: {}, score: {}".format(subject, scores[subject]))
            #print(score.keys())


    
    print ("\n======================")
"""


"""
student_list = [{'name': 'Leo', 'scores': {'math': 98.0, 'english': 87.0, 'chinese': 87.0}}, {'name': 'Jeff', 
'scores': {'math': 95.0, 'chinese': 54.0, 'english': 88.0}}]


student_info = {'name': 'Leo', 'scores': {'math': 98.0, 'english': 87.0, 'chinese': 87.0}}
print("name : {}".format(student_info["name"]))
subject = student_info["scores"]
print("type : {}".format(type(subject)))
print("subject : {}".format(subject["math"]))


#print(student_info["math"])
main(student_list)
"""
