from Dice import Dice
from CalAvgPoint import CalAvgPoint

dice1 = Dice()
dice2 = Dice(4)

result = CalAvgPoint(10000, dice1, dice2).execute()

print(result)
