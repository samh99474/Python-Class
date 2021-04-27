def main():
    print("Quiz 1")
    num = int(input('please enter a value:'))
    for i in range(num+1,2,-1):
        for j in range(1,i):
            print("*", end =" ")
        print()

    for i in range(1,num+1):
        for j in range(0,i):
            print("*", end =" ")
        print()
