class AddStu :
    def __init__(self, student_list):
        self.student_info = {}
        self.exit_flag = 1
        self.student_list = student_list

    def execute(self):
        name = input("  Please input a student's name: ")
    
        exit_flag = 1
        subject_dict = {}
        while(exit_flag == 1) : 
            subject = input("  Please input a subject name or exit for ending: ")
            if(subject == "exit") :
                break
            else : 
                score = self.scores_check(name, subject)
                if(score > 0) :
                    subject_dict[subject] = score

        self.student_info["name"] = name
        self.student_info["scores"] = subject_dict
        self.student_list.append(self.student_info)
        print("    Add {} success".format(self.student_info))
        return self.student_list

    def scores_check(self, name, subject) :
        input_success = False
        while(not(input_success)) :
            try :
                score = float(input("  Please input {}'s {} score or < 0 for discarding the subject: ".format(name, subject)))
                input_success = True
                
            except Exception as e:
                print("  Wrong format with reason {}, try again".format(e))
        
        return score



"""
def main(student_list):
    #print("add_stu")
    #print("student_list : {}".format(student_list))
    student_info = {}
    name = input("  Please input a student's name: ")
    
    exit_flag = 1
    subject_dict = {}
    while(exit_flag == 1) : 
        subject = input("  Please input a subject name or exit for ending: ")
        if(subject == "exit") :
            break
        else : 
            score = score_check(name, subject)
            if(score > 0) :
                subject_dict[subject] = score

    student_info["name"] = name
    student_info["scores"] = subject_dict
    student_list.append(student_info)
    print("    Add {} success".format(student_info))

def score_check(name, subject) : 
    input_success = False
    while(not(input_success)) :
        try :
            score = float(input("  Please input {}'s {} score or < 0 for discarding the subject: ".format(name, subject)))
            input_success = True
            
        except Exception as e:
            print("  Wrong format with reason {}, try again".format(e))
    
    return score
"""


"""
student_list = []
input_key = 1
while(input_key) : 
    main(student_list)
    print("student_list_len : {}".format(len(student_list)))
    for student_info in student_list :
        print("student_info : \n{}".format(student_info))
    input_key = input("int : ")

print("student_list : {}".format(student_list))
"""







