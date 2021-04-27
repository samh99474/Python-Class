def main(student_list):
    try:
        print("顯示所有資料")
        print(student_list)
    except Exception as e:      #若try有錯誤，則執行except
        print("The exception {} occurs.".format(e))
    finally:
        return student_list