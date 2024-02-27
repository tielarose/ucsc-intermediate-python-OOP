# Dice - count totals in user-defined number of rounds
import random

MIN_ROLL = 2
MAX_ROLL = 12

class Bin():
    def __init__(self, binIdentifier):
        # This is run when you create a Bin object
        pass

    def reset(self):
        # This is called when at start and at restart
        pass

    def increment(self):
        # Called when the roll total is the value of the binIdentifier
        pass

    def show(self, nRoundsDone):
        # Called at the end to show the contents of this bin
        pass


class BinManager():
    def __init__(self):
        # Create an empty dictionary
        self.binDict = {}
        # Add entries where each key is the roll total, and value is a Bin object
        for rollTotal in range(MIN_ROLL, MAX_ROLL + 1):
            oBin = Bin(rollTotal)
            self.binDict[rollTotal] = oBin

    def reset(self):
        # Tell each Bin object to reset itself
        pass

    def currentRoll(self, rollTotal):
        # Tell the appropriate Bin object to increment itself
        pass

    def show(self, nRoundsDone):
        # Tell each Bin objects to show itself
        pass


# Main code
# Create the Bin Manager
oBinMgr = BinManager()

while True:
    nRounds = input('How many rounds do you want to do? (or Enter to exit): ')
    if nRounds == '':
        break
    nRounds = int(nRounds)

    oBinMgr.reset()
        
    # ADD CODE:
    # For each round (build a loop):
    #     roll two dice
    #     calculate the total
    #     and tell the Bin Manager about the current roll

    print()
    print('After', nRounds, 'rounds:')
    # Tell the Bin Manager to show everything
    oBinMgr.show(nRounds)
    print()

print('OK bye')
