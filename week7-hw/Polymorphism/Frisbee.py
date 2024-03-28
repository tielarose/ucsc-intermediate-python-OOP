# Frisbee object

import pygame
import pygwidgets
import random


class Frisbee:
    def __init__(self, window):
        self.x = 30
        self.y = 30
        self.image = pygwidgets.Image(window, (self.x, self.y), "images/Frisbee.png")
        self.rect = self.image.getRect()
        self.isRotating = False
        self.nFrames = 0

    def clickedInside(self, mousePoint):
        if self.rect.collidepoint(mousePoint):
            self.nFrames = 30
            self.isRotating = True

    def update(self):
        if not self.isRotating:
            return

        self.image.rotate(15)
        self.nFrames -= 1
        if self.nFrames == 0:
            self.isRotating = False

    def draw(self):
        self.image.draw()
