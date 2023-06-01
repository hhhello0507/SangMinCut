import pygame
from src.util.constants import *
from src.util.resource import *
from src.entity.Player import *
from src.wiget.Button import *
from src.manager.BulletManager import *
from src.manager.SangMinManager import *
from src.manager.StageManager import *
from src.manager.GalManager import *
from src.manager.HpPotionManager import *
from src.manager.XpPotionManager import *
import math

class DrawManager:
    startButton = Button(SCREEN_WIDTH - BUTTON_WIDTH, SCREEN_HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
    settingButton = Button(0, 0, SETTING_BUTTON_WIDTH, SETTING_BUTTON_HEIGHT)
    soundButton = Button(0, 0, SOUND_BUTTON_WIDTH, SOUND_BUTTON_HEIGHT)
    closeButton = Button(100, 0, CLOSE_BUTTON_WIDTH, CLOSE_BUTTON_HEIGHT)
    backButton = Button(200, 0, BACK_BUTTON_WIDTH, BACK_BUTTON_HEIGHT)
    toMainButton = Button(200, 0, TOMAIN_BUTTON_WIDTH, TOMAIN_BUTTON_HEIGHT)

    display = None
    screen = None
    font = None

    mainStartText = None

    hpBarText = None
    hpText = None

    xpBarText = None
    xpText = None

    stageBarText = None
    stageText = None


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
    # updateGame


    # drawMain
    def drawMain(self):
        self.drawMainMap(self)

    # drawGame
    def drawGame(self):
        DrawUpdateManager.updateGame(DrawUpdateManager)
        self.drawGameMap(self)
        self.drawHPBar(self)
        self.drawXPBar(self)
        self.drawStage(self)
        self.display.update()

    def drawGameOver(self):
        self.drawGameOverMap(self)
        self.display.update()

    def drawMainMap(self):
        self.screen.blit(IMG_BUTTON, (self.startButton.xPos, self.startButton.yPos))
        self.screen.blit(self.mainStartText,
                             (self.startButton.xPos + 40, self.startButton.yPos + 20))
        self.display.update()



    def drawGameMap(self):
        self.screen.blit(IMG_BACKGROUND, (0, 0))
        self.screen.blit(IMG_PLAYER, (Player.xPos, Player.yPos))
        self.screen.blit(IMG_SETTING_BUTTON, (self.settingButton.xPos, self.settingButton.yPos))
        for bullet in BulletManager.bulletList:
            self.screen.blit(IMG_BULLET, (bullet.xPos, bullet.yPos))
        for sangMin in SangMinManager.sangMinList:
            self.screen.blit(IMG_SANGMIN, (sangMin.xPos, sangMin.yPos))
        for gal in GalManager.galList:
            self.screen.blit(IMG_GAL, (gal.xPos, gal.yPos))
        for hpPotion in HpPotionManager.hpPotionList:
            self.screen.blit(IMG_HP_POTION, (hpPotion.xPos, hpPotion.yPos))
        for xpPotion in XpPotionManager.xpPotionList:
            self.screen.blit(IMG_XP_POTION, (xpPotion.xPos, xpPotion.yPos))

    def drawHPBar(self):
        self.screen.blit(self.hpBarText, (Player.xPos, Player.yPos))
    def drawXPBar(self):
        self.screen.blit(self.xpBarText, (40, SCREEN_HEIGHT - 100))

    def drawStage(self):
        self.screen.blit(self.stageBarText, (200, 40))

    def drawSettingMap(self):
        self.screen.blit(IMG_SOUND_BUTTON, (self.soundButton.xPos, self.soundButton.yPos))
        self.screen.blit(IMG_CLOSE_BUTTON, (self.closeButton.xPos, self.closeButton.yPos))
        self.screen.blit(IMG_BACK_BUTTON, (self.backButton.xPos, self.backButton.yPos))
        self.display.update()

    # 임시 이미지
    def drawGameOverMap(self):
        # 검열
        # self.screen.blit(IMG_GAMEOVER_BACKGROUND, (0, 0))
        self.screen.blit(IMG_BUTTON, (self.startButton.xPos, self.startButton.yPos))
        self.screen.blit(self.mainStartText,
                             (self.startButton.xPos + 40, self.startButton.yPos + 20))

class DrawUpdateManager():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.data = data
            cls._init = True

    def updateHpText(self):
        DrawManager.hpText = f"{Player.playerHp} / {PLAYER_INIT_HP}"
        DrawManager.hpBarText = DrawManager.font.render(DrawManager.hpText, False, (255, 255, 0))

    def updateXpText(self):
        DrawManager.xpText = "*" * (int(Player.playerXp * (PLAYER_XP_TEXT_WIDTH / Player.playerMaxXp))) + "-" * (int((Player.playerMaxXp - Player.playerXp) *  (PLAYER_XP_TEXT_WIDTH / Player.playerMaxXp)))
        DrawManager.xpBarText = DrawManager.font.render(DrawManager.xpText, False, (255, 255, 0))

    def updateStageText(self):
        DrawManager.stageText = f"{StageManager.stage} STAGE ^ NEXT STAGE: {math.ceil(StageManager.beforeTime + StageManager.nextStageTime - time.time())}"
        DrawManager.stageBarText = DrawManager.font.render(DrawManager.stageText, False, (255, 255, 0))

    def updateGame(self):
        self.updateXpText(self)
        self.updateHpText(self)
        self.updateStageText(self)
