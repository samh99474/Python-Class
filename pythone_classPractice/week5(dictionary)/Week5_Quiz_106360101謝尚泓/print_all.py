def main(student_dict):
    try:
        print ("\n==== student list ====\n")
        for student_dict_name, student_dict_info in student_dict.items():
            print("Name: ", student_dict_name)
            for key in student_dict_info:
                print("   subject:"+ key + ', score: ', student_dict_info[key])
        print ("======================")
        
    except Exception as e:      #若try有錯誤，則執行except
        print("The exception {} occurs.".format(e))
    finally:
        return student_dict

"""student_dict = {'kelly': {'english': 60, 'chinese': 90},
          'apple': {'english': 62, 'chinese': 80}}
main(student_dict)"""