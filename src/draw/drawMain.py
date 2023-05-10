from src.info.drawInfo import *
from src.util.resource import *
def drawMain():
    screen.blit(IMG_BUTTON, (startButton.xPos, startButton.yPos))
    screen.blit(mainStartText, (startButton.xPos + 40, startButton.yPos + 20))
    display.update()