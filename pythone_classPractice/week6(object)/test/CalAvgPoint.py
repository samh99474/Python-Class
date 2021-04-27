class CalAvgPoint:
    def __init__(self, counts, dice1, dice2):
        self.counts = counts
        self.dice1 = dice1
        self.dice2 = dice2
    
    def execute(self):
        total = self.run_rolls(2)

        return total/self.counts

    def run_rolls(self, dummy):
        total = 0
        print(dummy)
        for _ in range(self.counts):
            total += (self.dice1.roll() + self.dice2.roll())

        return total 