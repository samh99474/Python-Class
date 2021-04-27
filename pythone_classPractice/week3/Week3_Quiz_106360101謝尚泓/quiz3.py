def main():
    print("Quiz 3")

    lines = int(input("輸入要打的行數(奇數):"))
    if lines % 2 == 0:
        print('您輸入的不是奇數')
        return False
        """Exit
        import sys
        sys.exit(0)
        """

    half_lines = lines // 2 + 1
    # 打印上半
    for i in range(half_lines):
        print(" " * (half_lines - i), end="") #end=""表示不換行
        if i == 0:
            print("*")
        else:
            print("*", end="")
            print("*" * (2 * i - 1), end="")
            #print(" " * (2 * i - 1), end="")
            print("*")
            
    # 打印下半
    for i in range(half_lines - 1):
        print(" " * (i + 2), end="")
        if i == half_lines - 2:
            print("*")
        else:
            print("*", end="")
            print("*" * (lines - 4 - 2 * i), end="")
            #print(" " * (lines - 4 - 2 * i), end="")
            print("*")
