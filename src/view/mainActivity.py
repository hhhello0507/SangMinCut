import pygame

from src.info.lifeInfo import *
from src.draw.drawMain import *
from src.draw.drawGame import *
from src.info.drawInfo import *

def initPygame():
    pygame.init()
    DrawInfo.init(DrawInfo)


# view
def onMouseClick():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (xMousePos, yMousePos) = pygame.mouse.get_pos()
            if DrawInfo.startButton.xPos <= xMousePos <= DrawInfo.startButton.xPos + DrawInfo.startButton.width and DrawInfo.startButton.yPos <= yMousePos <= DrawInfo.startButton.yPos + DrawInfo.startButton.height:
                LifeInfo.isMain = False
                LifeInfo.isPlaying = True
        if event.type == pygame.QUIT:
            exit(0)


def startMain():
    # init
    initPygame()

    while LifeInfo.isMain:
        # event
        onMouseClick()

        # manager
        # pass

        # draw
        drawMain()
