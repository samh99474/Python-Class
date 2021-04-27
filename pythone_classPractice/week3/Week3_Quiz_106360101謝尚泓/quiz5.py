#終極密碼
"""
Python傳值不傳址, 看得到吃不到.
Python是函數(function)式語言, 函數的意義如同變數, 在函數中的變數範圍僅及於函數的範圍.
Python並無變數宣告(declaration)的機制, 必須透過等號對變數賦值(assignment)在記憶體中定址.

可以用global來定址
"""
import random

def main():
       global ans
       global maxTimes
       global within_maxTimes
       ans = random.randint(1,100)
       maxTimes = 6
       within_maxTimes = True
       print("Quiz 5")
       guessing()

def guessing():
       global min
       global max
       global times
       min = 0
       max = 100
       times = 0

       while(True):
              times = times+1
              if (times > maxTimes):
                     within_maxTimes == False
                     print("Achieve limitted 超過6次了")
                     return False
              else:
                     guess = int(input("Please input a number that between %d ~ %d : "%(min, max)))
                     if (guess > ans):
                            max = guess
                     if (guess < ans):
                            min = guess
                     if (guess == ans):
                            print("Bingo!! You passed")
                            break
