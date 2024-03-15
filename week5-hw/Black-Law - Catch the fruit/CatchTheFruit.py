# Catch the fruit

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
from Fruit import *  # bring in the Fruit class code
from Basket import *  # bring in the Basket class code
import pygwidgets

# 2 - Define constants
BLACK = (0, 0, 0)
LIME = (0, 255, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
FRAMES_PER_SECOND = 30
TYPES_OF_FRUIT = ["apple", "banana", "cherry", "grapes", "strawberry", "pear"]

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  # set the speed (frames per second)

# 4 - Load assets: image(s), sounds, etc.
oDisplay = pygwidgets.DisplayText(window, (WINDOW_WIDTH - 120, 10), "", fontSize=30)

# 5 - Initialize variables
backgroundImage = pygwidgets.Image(window, (0, 0), "images/background.png")
oBasket = Basket(window, WINDOW_WIDTH, WINDOW_HEIGHT)

fruitList = []
for fruitType in TYPES_OF_FRUIT:
    points = -100 if fruitType == "pear" else 15
    oFruit = Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, fruitType)
    fruitList.append(oFruit)

oRestartButton = pygwidgets.TextButton(window, (5, 5), "Restart")

score = 0


# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oRestartButton.handleEvent(event):  # ckicked on the Restart button
            print("User pressed the Restart button")

        # Add "continuous mode" code here to check for left or right arrow keys
        # If you get one, tell the basket to move itself appropriately

    # Check for user pressing keys
    keyPressedTuple = pygame.key.get_pressed()
    left = keyPressedTuple[pygame.K_LEFT]  # left=1 if left key was pressed, else 0
    right = keyPressedTuple[pygame.K_RIGHT]  # right=1 if right key was pressed, else 0

    if left or right:
        oBasket.move(left=left, right=right)

    # 8 - Do any "per frame" actions
    for oFruit in fruitList:
        oFruit.update()  # tell each fruit to update itself

    basketRect = oBasket.getRect()

    fruitRect = oFruit.getRect()
    if basketRect.colliderect(fruitRect):
        print("Fruit has collided with the basket")

    oDisplay.setValue("Score:" + str(score))

    # 9 - Clear the screen before drawing it again
    backgroundImage.draw()

    # 10 - Draw the screen elements
    for oFruit in fruitList:
        oFruit.draw()  # tell each ball to draw itself

    oRestartButton.draw()
    oBasket.draw()
    oDisplay.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount
