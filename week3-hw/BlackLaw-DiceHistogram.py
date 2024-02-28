# Dice - count totals in user-defined number of rounds
import random

MIN_ROLL = 2
MAX_ROLL = 12


class Bin:
    def __init__(self, binIdentifier):
        self.name = binIdentifier
        self.qty = 0

    def reset(self):
        self.qty = 0

    def increment(self):
        self.qty += 1

    def show(self, nRoundsDone):
        percent = round((self.qty // nRoundsDone) * 100)
        print(f"{self.name}: {'*' * percent}{percent}%    ({self.qty})")


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

    def currentRoll(self, rollTotal):
        oBin = self.binDict[rollTotal]
        oBin.increment()

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
        rollTotal = random.choice(diceValues) + random.choice(diceValues)
        oBinMgr.currentRoll(rollTotal)

    print()
    print("After", nRounds, "rounds:")
    # Tell the Bin Manager to show everything
    oBinMgr.show(nRounds)
    print()

print("OK bye")
