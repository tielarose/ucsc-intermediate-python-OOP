# Card Class

import pygwidgets

class Card():

    def __init__(self, window, rank, suit, value):
        # must add code here to save away parameters in instance variables
        # and create two Image objects, one for the current card, one for the backOfCard
        pass     # you can remove this line when you add your own

    # You can remove the print statement below
    # These are just place holders.



    def conceal(self):
        print('Must conceal the card here')

    def setLoc(self, locTuple):
        print('Called setLoc method, passed in', locTuple)

    def reveal(self):
        print('Must reveal card here')

    def getName(self):
        print('Get the name of the card here')

    def getValue(self):
        print('Get the value of the card here')

    def draw(self):
        print('Draw the card here')

    # No need to change this
    def getCardNameAndValue(self):
        return ("CardName", 0)
