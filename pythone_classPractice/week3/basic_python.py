"""
多行註解

1.除法
/ for float divison
// for integer division (若有小數點，會自動進位)

2.乘法**
3.in python ,we used to declare global constant,not global variable
4.python 排版要正確才能執行

---------------------------------------重要觀念-------------------------------
Python傳值不傳址, 看得到吃不到.
Python是函數(function)式語言, 函數的意義如同變數, 在函數中的變數範圍僅及於函數的範圍.
Python並無變數宣告(declaration)的機制, 必須透過等號對變數賦值(assignment)在記憶體中定址.

可以用global來定址
"""
import random
s = "歡迎使用"
container = None
container_boolean = False
a = 8

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
name = input('pleas input your name') #return string
age = int(input('pleas input your age')) #return string,and format it

print('da')

if a >=10 and a<=20:
    print('Grade is: A')
elif score >= 80:
    print('Grade is: B')
elif score >= 70:
    print('Grade is: C')
elif score >= 60:
    print('Grade is: D')
else:
    print('Grade is: F')
# 特殊
if container is True: # is => use to judge  Boolean or None
    print("")
###############While
    
while(container_boolean):
    for var in range(5) #[0,1,2,3,4]
    for var in range(1,5) #[1,2,3,4,5]
    for var in range(1,5,2) #[1,3,5,7,9]
    print('Grade is: F')

###############Function
def main():
    function_name(0.01) #call function (rete)
    function_name(0.01, period = 10) #call function (rete , period = 10):

def function_name(rete , period = 15):
    computeNum = rete
    number = random.randint(1, 10)#要先import random
    print('def function_name')
    return computeNum,number




