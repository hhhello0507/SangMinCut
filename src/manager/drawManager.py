from src.info.drawInfo import *
from src.util.resource import *
from src.entity.player import *
from src.manager.bulletManager import *
from src.manager.sangMinManager import *

class DrawManager:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.data = data
            cls._init = True

    def drawGame(self):
        DrawInfo.screen.blit(IMG_BACKGROUND, (0, 0))
        DrawInfo.screen.blit(IMG_PLAYER, (Player.xPos, Player.yPos))
        DrawInfo.screen.blit(IMG_SETTING, (DrawInfo.settingButton.xPos, DrawInfo.settingButton.yPos))
        for bullet in BulletManager.bulletList:
            DrawInfo.screen.blit(IMG_BULLET, (bullet.xPos, bullet.yPos))
        for sangMin in SangMinManager.sangMinList:
            DrawInfo.screen.blit(IMG_SANGMIN, (sangMin.xPos, sangMin.yPos))
        DrawInfo.display.update()

    def drawMain(self):
        DrawInfo.screen.blit(IMG_BUTTON, (DrawInfo.startButton.xPos, DrawInfo.startButton.yPos))
        DrawInfo.screen.blit(DrawInfo.mainStartText, (DrawInfo.startButton.xPos + 40, DrawInfo.startButton.yPos + 20))
        DrawInfo.display.update()

    def drawSetting(self):
        DrawInfo.screen.blit(IMG_SOUND_BUTTON, (DrawInfo.soundButton.xPos, DrawInfo.soundButton.yPos))
        DrawInfo.screen.blit(IMG_CLOSE_BUTTON, (DrawInfo.closeButton.xPos, DrawInfo.closeButton.yPos))
        DrawInfo.screen.blit(IMG_BACK_BUTTON, (DrawInfo.backButton.xPos, DrawInfo.backButton.yPos))
        DrawInfo.display.update()