import pygame
from pygame.locals import *
import random


# DROP CLASS
class Drop:

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.dropImage = pygame.image.load("images/drop.png")
        # A rect is made up of [x, y, width, height]
        dropRect = self.dropImage.get_rect()
        self.width = dropRect[2]
        self.height = dropRect[3]
        self.maxWidth = windowWidth - self.width

        # Pick a random starting position
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(-(self.height - 5), 0)

        # Choose a random speed in the y direction
        self.ySpeed = random.randrange(3, 6)

    def update(self):
        # if drop falls off the bottom of the screen, restart above the top of the screen
        if self.y > self.windowHeight:
            self.y = -self.height

        # update y position based on speed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.dropImage, (self.x, self.y))
