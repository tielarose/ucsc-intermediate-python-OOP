# Square object

import pygame
import pygwidgets
import random

# set up the colors
PINK1 = (255, 182, 193)
PINK2 = (175, 59, 110)
PINK3 = (236, 132, 177)


class Square:
    def __init__(self, window):
        self.window = window
        self.x = 110
        self.y = 350
        self.side = random.randrange(10, 100)
        self.color = random.choice((PINK1, PINK2, PINK3))
        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)
        self.nFrames = 0
        self.newSize = self.side

    def clickedInside(self, mousePoint):
        if self.rect.collidepoint(mousePoint):
            self.nFrames = 10
            self.newSize = random.randrange(10, 100)

    def update(self):
        if self.side == self.newSize:
            return

        self.nFrames -= 1
        if self.nFrames == 0:
            self.side = self.newSize
        else:
            self.side += (self.newSize - self.side) // self.nFrames

        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)

    def draw(self):
        pygame.draw.rect(
            self.window,
            self.color,
            (self.x, self.y, self.side, self.side),
        )
