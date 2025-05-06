# File Utama Game Tebak Kartu

import pygame
from pygame.locals import *
import sys
import pygwidgets
from Game import *

# definisikan nilai konstanta (ukuran layar untuk game)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30

# inisilisasi
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

background = pygwidgets.Image(window, (0, 0), 'images/background.png')
newGameButton = pygwidgets.TextButton(window, (20, 520), 'Game Baru', width=100, height=55)
higherButton = pygwidgets.TextButton(window, (540, 520), 'Higher', width=100, height=55)
lowerButton = pygwidgets.TextButton(window, (340, 520), 'Lower', width=100, height=55)
quitButton = pygwidgets.TextButton(window, (880, 520), 'Keluar', width=100, height=55)

oGame = Game(window)

# looping forever
while True:
    for event in pygame.event.get():
        if ((event.type == QUIT) or ((event.type == KEYDOWN) and (event.key == K_ESCAPE)) or (quitButton.handleEvent(event))):
            pygame.quit()
            sys.exit()

        if newGameButton.handleEvent(event):
            oGame.reset()
            lowerButton.enable()
            higherButton.enable()

        if higherButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(HIGHER)
            if gameOver:
                lowerButton.disable()
                higherButton.disable()

        if lowerButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(LOWER)
            if gameOver:
                lowerButton.disable()
                higherButton.disable()

    background.draw()

    oGame.draw()
    newGameButton.draw()
    higherButton.draw()
    lowerButton.draw()
    quitButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)