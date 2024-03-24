# Card Class

import pygwidgets


class Card:

    def __init__(self, window, rank, suit, value):
        # must add code here to save away parameters in instance variables
        # and create two Image objects, one for the current card, one for the backOfCard
        self.window = window
        self.rank = rank
        self.suit = suit
        self.value = value
        self.cardName = f"{rank} of {suit}"
        self.imagesDict = {
            "frontOfCard": f"{rank} of {suit}.png",
            "backOfCard": "BackOfCard.png",
        }
        self.currImage = pygwidgets.ImageCollection(
            window, (0, 0), self.imagesDict, "backOfCard", path="images/"
        )

    def conceal(self):
        self.currImage.replace("backOfCard")

    def setLoc(self, locTuple):
        self.currImage.setLoc(locTuple)

    def reveal(self):
        self.currImage.replace("frontOfCard")

    def getName(self):
        return self.cardName

    def getValue(self):
        return self.value

    def draw(self):
        self.currImage.draw()

    # No need to change this
    def getCardNameAndValue(self):
        return ("CardName", 0)
