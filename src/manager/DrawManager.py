import pygame
from src.util.constants import *
from src.util.resource import *
from src.entity.Player import *
from src.wiget.Button import *
from src.manager.BulletManager import *
from src.manager.SangMinManager import *

class DrawManager:
    startButton = Button(SCREEN_WIDTH - BUTTON_WIDTH, SCREEN_HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
    settingButton = Button(0, 0, SETTING_WIDTH, SETTING_HEIGHT)
    soundButton = Button(0, 0, SOUND_BUTTON_WIDTH, SOUND_BUTTON_HEIGHT)
    closeButton = Button(100, 0, CLOSE_BUTTON_WIDTH, CLOSE_BUTTON_HEIGHT)
    backButton = Button(200, 0, BACK_BUTTON_WIDTH, BACK_BUTTON_HEIGHT)

    display = None

    screen = None

    font = None
    mainStartText = None
    hpBarText = None
    hpText = None


    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.data = data
            cls._init = True

    def init(self):
        self.display = pygame.display
        self.display.set_caption("SangMinCut!!")

        self.screen = self.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.font = pygame.font.Font("../res/font/arial.ttf", 30)
        self.mainStartText = self.font.render("start", False, (20, 20, 20))

    def updateHpText(self):
        self.hpText = f"{Player.playerHP} / {PLAYER_INIT_HP}"
        self.hpBarText = self.font.render(self.hpText, False, (255, 255, 0))

    def drawGame(self):
        self.screen.blit(IMG_BACKGROUND, (0, 0))
        self.screen.blit(IMG_PLAYER, (Player.xPos, Player.yPos))
        self.screen.blit(IMG_SETTING, (self.settingButton.xPos, self.settingButton.yPos))
        for bullet in BulletManager.bulletList:
            self.screen.blit(IMG_BULLET, (bullet.xPos, bullet.yPos))
        for sangMin in SangMinManager.sangMinList:
            self.screen.blit(IMG_SANGMIN, (sangMin.xPos, sangMin.yPos))
        self.display.update()

    def drawMain(self):
        self.screen.blit(IMG_BUTTON, (self.startButton.xPos, self.startButton.yPos))
        self.screen.blit(self.mainStartText,
                             (self.startButton.xPos + 40, self.startButton.yPos + 20))
        self.display.update()

    def drawSetting(self):
        self.screen.blit(IMG_SOUND_BUTTON, (self.soundButton.xPos, self.soundButton.yPos))
        self.screen.blit(IMG_CLOSE_BUTTON, (self.closeButton.xPos, self.closeButton.yPos))
        self.screen.blit(IMG_BACK_BUTTON, (self.backButton.xPos, self.backButton.yPos))
        self.display.update()

    def drawHPBar(self):
        self.screen.blit(self.hpBarText, (Player.xPos, Player.yPos))
        self.display.update()