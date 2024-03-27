# Rectangle class

import pygame
import random

# set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Rectangle:

    def __init__(self, window):
        self.window = window
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.color = random.choice((RED, GREEN, BLUE))
        # get window height and width
        w, h = pygame.display.get_surface().get_size()
        self.x = random.randrange(00, w - self.width)
        self.y = random.randrange(50, h - self.height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.type = "Rectangle"

    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked

    def getType(self):
        return self.type

    def getArea(self):
        theArea = self.width * self.height
        return theArea

    def draw(self):
        pygame.draw.rect(
            self.window,
            self.color,
            (self.x, self.y, self.width, self.height),
        )
