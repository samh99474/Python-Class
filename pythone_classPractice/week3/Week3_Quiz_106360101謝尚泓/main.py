"""
學號:106360101
姓名:謝尚泓
"""
import quiz1, quiz2, quiz3, quiz4, quiz5

def main():
    keep_going = "y"
    while keep_going == "y":
        select_result = print_menu()
        if select_result == 1:
            quiz1.main()
        elif select_result == 2:
            quiz2.main()
        elif select_result == 3:
            quiz3.main()
        elif select_result == 4:
            quiz4.main()
        elif select_result == 5:
            quiz5.main()
        else:
            print ("No such selection")

        print()
        keep_going = input("Test again (y)?")

def print_menu():
    print("============ Quzi =============")
    print("1. Print double triangle")
    print("2. Print spacing triangle")
    print("3. Print diamond")
    print("4. Print grid")
    print("5. Guessing game")
    selection = int(input("Please select: "))
    return selection

main()