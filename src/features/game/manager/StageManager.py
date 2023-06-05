from src.features.game.manager.SangMinManager import *
from src.util.resource import *
import time
class StageManager:
    def __init__(self):
        self.stage = 1
        self.beforeTime = -1
        self.nextStageTime = 10
        self.background = IMG_GAME_BACKGROUND1

    def manageStage(self):
        self.__stageIncrease()
        self.__updateSangMinCreateTime()
        self.__updateBackgroundImage()

    def __stageIncrease(self):
        if self.beforeTime == -1:
            self.beforeTime = time.time()

    def __updateSangMinCreateTime(self):
        now = time.time()
        sangMinManager = Container.container["sangMinManager"]
        if self.beforeTime + self.nextStageTime < now:
            self.nextStageTime += 2
            self.stage += 1
            self.beforeTime = now
            sangMinManager.sangMinCreateTime1 *= 0.8
            sangMinManager.sangMinCreateTime2 *= 0.8
            print("sangMinCreateTime1 - %.6f sangMinCreateTime2 - %.6f" % (sangMinManager.sangMinCreateTime1, sangMinManager.sangMinCreateTime2))

    def __updateBackgroundImage(self):
        if self.stage == 3:
            self.background = IMG_GAME_BACKGROUND2
        if self.stage == 6:
            self.background = IMG_GAME_BACKGROUND3
        if self.stage == 9:
            self.background = IMG_GAME_BACKGROUND4
        if self.stage == 12:
            self.background = IMG_GAME_BACKGROUND5

    def init(self):
        self.backround = IMG_GAME_BACKGROUND1
        self.stage = 1
        self.beforeTime = -1
        self.nextStageTime = 10