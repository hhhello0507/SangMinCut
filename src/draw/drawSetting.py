from src.info.drawInfo import *
from src.util.resource import *
def drawSetting():
    DrawInfo.screen.blit(IMG_SOUND_BUTTON, (DrawInfo.soundButton.xPos, DrawInfo.soundButton.yPos))
    DrawInfo.screen.blit(IMG_CLOSE_BUTTON, (DrawInfo.closeButton.xPos, DrawInfo.closeButton.yPos))
    DrawInfo.screen.blit(IMG_BACK_BUTTON, (DrawInfo.backButton.xPos, DrawInfo.backButton.yPos))
    DrawInfo.display.update()