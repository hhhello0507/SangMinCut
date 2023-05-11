from src.info.drawInfo import *
from src.util.resource import *


def drawMain():
    DrawInfo.screen.blit(IMG_BUTTON, (DrawInfo.startButton.xPos, DrawInfo.startButton.yPos))
    DrawInfo.screen.blit(DrawInfo.mainStartText, (DrawInfo.startButton.xPos + 40, DrawInfo.startButton.yPos + 20))
    DrawInfo.display.update()