class ModifyStu :
    def __init__(self, student_list) :
        self.student_list = student_list

    def execute(self) :
        #print("mofify_stu")
        name = input("  Please input a student's name: ")

        search_people = False
        for student_info in self.student_list :
            if student_info["name"] == name :
                search_people = True
                position = self.student_list.index(student_info)
                #print("position : {}".format(position))
                scores = student_info["scores"]
                #print(scores)
                #print(scores.keys())
                print("  current subject are ", end = "")
                for subject in scores :
                    print("{} ".format(subject), end = "")
                
                subject_change = input("\n\n  Please input a subject you want to change: ")
                new_score, search_fail = self.score_check(name, scores, subject_change)

                if new_score > 0 :
                    scores[subject_change] = new_score
                    student_info["scores"] = scores
                    self.student_list[position] = student_info
                    if not search_fail : 
                        print("    Modify [{}, {}, {}] success".format(name, subject_change, new_score))

        if not search_people :
            print("    The name {} is not found".format(name))

        return self.student_list
    
    def score_check(self, name, scores, subject_change) :
        search_fail = True
        for subject in scores :
            if subject == subject_change :
                search_fail = False

        input_success = False
        while(not(input_success)) :
            try :
                if search_fail :
                    score = float(input("  Add a new subject for {} please input {} score or < 0 for discarding the subject: ".format(name, subject_change)))
                else :
                    score = float(input("  Please input {}'s new score: ".format(subject_change)))

                input_success = True
                
            except Exception as e:
                print(" Wrong format with reason {}, try again".format(e))
        
        return score, search_fail

"""
def main(student_list):
    #print("mofify_stu")
    name = input("  Please input a student's name: ")

    search_people = False
    for student_info in student_list :
        if student_info["name"] == name :
            search_people = True
            position = student_list.index(student_info)
            #print("position : {}".format(position))
            scores = student_info["scores"]
            #print(scores)
            #print(scores.keys())
            print("  current subject are ", end = "")
            for subject in scores :
                print("{} ".format(subject), end = "")
            
            subject_change = input("\n\n  Please input a subject you want to change: ")
            new_score, search_fail = score_check(name, scores, subject_change)

            if new_score > 0 :
                scores[subject_change] = new_score
                student_info["scores"] = scores
                student_list[position] = student_info
                if not search_fail : 
                    print("    Modify [{}, {}, {}] success".format(name, subject_change, new_score))

    if not search_people :
        print("    The name {} is not found".format(name))
            

def score_check(name, scores, subject_change) : 
    search_fail = True
    for subject in scores :
        if subject == subject_change :
            search_fail = False

    input_success = False
    while(not(input_success)) :
        try :
            if search_fail :
                score = float(input("  Add a new subject for {} please input {} score or < 0 for discarding the subject: ".format(name, subject_change)))
            else :
                score = float(input("  Please input {}'s new score: ".format(subject_change)))

            input_success = True
            
        except Exception as e:
            print(" Wrong format with reason {}, try again".format(e))
    
    return score, search_fail
"""


"""
student_list = [{'name': 'Leo', 'scores': {'math': 98.0, 'english': 87.0, 'chinese': 87.0}}, {'name': 'Jeff', 
'scores': {'math': 95.0, 'chinese': 54.0, 'english': 88.0}}]

print("Before : \n{}".format(student_list))
main(student_list)
print("After : \n{}".format(student_list))
"""

































