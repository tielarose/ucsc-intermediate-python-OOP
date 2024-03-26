# Triangle class

import pygame
import random

# set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Triangle():

    def __init__(self, window):
        self.window = window
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(0, 400)
        self.y = random.randrange(50, 400)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.type = 'Triangle'
        
    def clickedInside(self, mousePoint):
        inRect = self.rect.collidepoint(mousePoint)
        if not inRect:
            return False

        # Do some math to see if the point is inside the triangle
        xOffset = mousePoint[0] - self.x
        yOffset = self.y + self.height - mousePoint[1]
        if xOffset == 0:
            return True

        slope = yOffset / xOffset  # rise over run
        if slope > 1:
            return True
        else:
            return False

    def getType(self):
        return self.type

    def getArea(self):
        theArea = .5 * self.width * self.height
        return theArea

    def draw(self):
        pygame.draw.polygon(self.window, self.color, (\
            (self.x, self.y + self.height), \
            (self.x, self.y),\
            (self.x + self.width, self.y)))
