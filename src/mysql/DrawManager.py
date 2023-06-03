from src.util.constants import *
from src.wiget.ButtonView import *
from features.game.manager.StageManager import *
from features.game.manager.GalManager import *
from features.game.manager.HoJoonManager import *
from features.game.manager.HpPotionManager import *
from features.game.manager.XpPotionManager import *
import math

class DrawManager:
    #
    # toMainButton = ButtonView() \
    #     .setPos((0, 0)) \
    #     .setImageByPath("../res/image/player1.png") \
    #     .setScale((100, 100)) \
    #     .setText("설정") \
    #     .setTextPos((100, 100))

    mainStartText = None

    hpBarText = None
    hpText = None

    xpBarText = None
    xpText = None

    stageBarText = None
    stageText = None

    # drawMain
    # drawGame
    def drawGame(self):
        DrawUpdateManager.updateGame(DrawUpdateManager)
        self.drawHPBar()
        self.drawXPBar()
        self.drawStage()
        self.display.update()

    def drawGameOver(self):
        self.drawGameOverMap(self)
        self.display.update()

    def drawHPBar(self):
        self.screen.blit(self.hpBarText, (Player.xPos, Player.yPos))
    def drawXPBar(self):
        self.screen.blit(self.xpBarText, (40, SCREEN_HEIGHT - 100))

    def drawStage(self):
        self.screen.blit(self.stageBarText, (200, 40))

    # 임시 이미지
    def drawGameOverMap(self):
        pass
        # 검열
        # self.screen.blit(IMG_GAMEOVER_BACKGROUND, (0, 0))
        # MainContainer.Container.screen.blit(IMG_BUTTON, (self.startButton.xPos, self.startButton.yPos))
        # self.screen.blit(self.mainStartText,
        #                      (self.startButton.xPos + 40, self.startButton.yPos + 20))

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
