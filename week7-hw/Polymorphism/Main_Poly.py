# Polymorphism Main program

# 1 - Import library
import pygame
from pygame.locals import *
import sys
import pygwidgets

from Star import *


# 2 Define constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 30
BGCOLOR = (0, 128, 128)

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

# 4 - Load assets: images(s), sounds, etc.


# 5 - Initialize variables
oResetButton = pygwidgets.TextButton(window, (300, 420), 'Reset star')
oStar = Star(window, (280, 200))

myList = [oStar]

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if oResetButton.handleEvent(event):
            oStar.reset()

        if event.type == MOUSEBUTTONDOWN:
            for object in myList:
                object.clickedInside(event.pos)


    # 8 - Do any "per frame" actions
    for object in myList:
        object.update()

    # 9 - Clear the window
    window.fill(BGCOLOR)

    # 10 - Draw all window elements
    for object in myList:
        object.draw()
    oResetButton.draw()

    # 11 - update the window
    pygame.display.update()
    
    # 12 - slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make Pygame wait the correct amount
