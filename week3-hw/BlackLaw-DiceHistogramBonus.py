# Dice - count totals in user-defined number of rounds
import random
from collections import defaultdict

MIN_ROLL = 2
MAX_ROLL = 12


class Bin:
    def __init__(self, binIdentifier):
        self.rollTotal = binIdentifier
        self.qty = 0
        self.waysToTotal = defaultdict(int)

    def reset(self):
        self.qty = 0

    def increment(self, die1, die2):
        self.qty += 1
        diceTup = (die1, die2) if die1 < die2 else (die2, die1)
        self.waysToTotal[diceTup] += 1

    def show(self, nRoundsDone):
        # print "histogram" line
        # ex: 4: ******** 8% (8329)
        percentOfTotalRounds = round((self.qty / nRoundsDone) * 100)
        print(
            f"{self.rollTotal}: {'*' * percentOfTotalRounds}{percentOfTotalRounds}%    ({self.qty})"
        )

        # print dice combinations and their respective rolls
        # 1 and 3 : 5550 = 66 %
        # 2 and 2 : 2779 = 33 %
        for die1, die2 in sorted(self.waysToTotal):
            numRolls = self.waysToTotal[(die1, die2)]
            percent = round((numRolls / self.qty) * 100)
            print(f"{die1} and {die2} : {numRolls} = {percent} %")


class BinManager:
    def __init__(self):
        # Create an empty dictionary
        self.binDict = {}
        # Add entries where each key is the roll total, and value is a Bin object
        for rollTotal in range(MIN_ROLL, MAX_ROLL + 1):
            oBin = Bin(rollTotal)
            self.binDict[rollTotal] = oBin

    def reset(self):
        for rollTotal in self.binDict:
            oBin = self.binDict[rollTotal]
            oBin.reset()

    def currentRoll(self, die1, die2):
        rollTotal = die1 + die2
        oBin = self.binDict[rollTotal]
        oBin.increment(die1, die2)

    def show(self, nRoundsDone):
        for rollTotal in range(MIN_ROLL, MAX_ROLL + 1):
            oBin = self.binDict[rollTotal]
            oBin.show(nRoundsDone)


# Main code
# Create the Bin Manager
oBinMgr = BinManager()

while True:
    nRounds = input("How many rounds do you want to do? (or Enter to exit): ")
    if nRounds == "":
        break
    nRounds = int(nRounds)

    oBinMgr.reset()

    for _ in range(nRounds):
        diceValues = [1, 2, 3, 4, 5, 6]
        die1 = random.choice(diceValues)
        die2 = random.choice(diceValues)
        oBinMgr.currentRoll(die1, die2)

    print()
    print("After", nRounds, "rounds:")
    # Tell the Bin Manager to show everything
    oBinMgr.show(nRounds)
    print()

print("OK bye")
