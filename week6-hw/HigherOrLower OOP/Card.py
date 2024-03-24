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
        # self.x = 0
        # self.y = 0
        # self.frontOfCard = pygwidgets.Image(
        #     window, (self.x, self.y), f"images/{rank} of {suit}.png"
        # )
        # self.backOfCard = pygwidgets.Image(
        #     window, (self.x, self.y), "images/BackOfCard.png"
        # )
        # self.showCard = False
        self.imagesDict = {
            "frontOfCard": f"{rank} of {suit}.png",
            "backOfCard": "BackOfCard.png",
        }
        self.currImage = pygwidgets.ImageCollection(
            window, (0, 0), self.imagesDict, "backOfCard", path="images/"
        )

    def conceal(self):
        # self.showCard = False
        self.currImage.replace("backOfCard")

    def setLoc(self, locTuple):
        x, y = locTuple
        # self.x = x
        # self.y = y
        # self.backOfCard.setLoc((self.x, self.y))
        # self.frontOfCard.setLoc((self.x, self.y))
        self.currImage.setLoc((x, y))

    def reveal(self):
        # self.showCard = True
        self.currImage.replace("frontOfCard")

    def getName(self):
        return f"{self.rank} of {self.suit}"

    def getValue(self):
        return self.value

    def draw(self):
        # if self.showCard:
        #     self.frontOfCard.draw()
        # else:
        #     self.backOfCard.draw()
        self.currImage.draw()

    # No need to change this
    def getCardNameAndValue(self):
        return ("CardName", 0)
