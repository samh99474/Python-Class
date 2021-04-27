def main():
    print("Quiz 2")
    num = int(input('please enter a value:'))
    blank = " "
    pic = "#"
    s = ""
    for i in range(0,num):
        s = pic+blank*i+pic
        print(s)
        blank = " "
