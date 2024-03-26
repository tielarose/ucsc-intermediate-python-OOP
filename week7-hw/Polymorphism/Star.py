# Star object

import pygame
import pygwidgets
import random


class Star():
    def __init__(self, window, loc):
        self.image = pygwidgets.Image(window, loc, 'images/Star.png')
        self.startX = loc[0]
        self.startY = loc[1]
        self.x = self.startX
        self.y = self.startY
        self.rect = self.image.getRect()
        self.moving = False

    def clickedInside(self, mousePoint):
        if self.rect.collidepoint(mousePoint):
            self.speedX = random.randrange(-10, 10)
            self.speedY = random.randrange(-10, 10)
            self.nFrames = 10
            self.moving = True

    def update(self):
        if not self.moving:
            return

        self.x = self.x + self.speedX
        self.y = self.y + self.speedY
        #print('New loc is:', (self.loc)
        self.image.setLoc((self.x, self.y))
        self.nFrames = self.nFrames - 1
        if self.nFrames == 0:
            self.moving = False
            self.rect = self.image.getRect()

    # This method is only needed in the Star class
    def reset(self):
        self.x = self.startX
        self.y = self.startY
        self.image.setLoc((self.x, self.y))

    def draw(self):
        self.image.draw()