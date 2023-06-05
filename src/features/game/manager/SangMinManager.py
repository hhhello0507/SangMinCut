from features.game.manager.BulletManager import *
from src.entity.Sangmin import *
import time
import random

class SangMinManager:
    def __init__(self):
        self.sangMinLoadTime = 0
        self.sangMinStartTime = time.time()
        self.sangMinList = []
        self.sangMinCreateTime1 = SANGMIN_CREATE_TIME_1
        self.sangMinCreateTime2 = SANGMIN_CREATE_TIME_2


    def manageSangMin(self):
        from Container import container
        activeSangMinList = []
        player = container["player"]
        bulletManager = container["bulletManager"]
        for (idx, sangMin) in enumerate(self.sangMinList):
            if not isObjectInMap(sangMin):
                sangMin.isActive = False

            # 플레이어와 충돌
            if sangMin.objectRect.colliderect(pygame.Rect(player.xPos, player.yPos, PLAYER_WIDTH, PLAYER_HEIGHT)):
                sangMin.isActive = False
                player.playerHp -= 1
                print("PlayerHP : -%d" % (player.playerHp))
            # 총알과 충돌
            for (bulletIdx, bullet) in enumerate(bulletManager.bulletList):
                if sangMin.objectRect.colliderect(bullet.objectRect):
                    sangMin.isActive = False
                    player.playerXp += 1
                    print("playerXP : +%d" % player.playerXp)
            sangMin.calcMove(player.xPos + PLAYER_WIDTH / 2, player.yPos + PLAYER_HEIGHT / 2, SANGMIN_SPEED)
            sangMin.move()
            if sangMin.isActive:
                activeSangMinList.append(sangMin)
        self.sangMinList = activeSangMinList

    def createSangMin(self):
        from Container import container

        player = container["player"]
        sangMinManager = container["sangMinManager"]
        nowTime = time.time()
        if nowTime - self.sangMinStartTime >= self.sangMinLoadTime:
            self.sangMinLoadTime = random.uniform(SANGMIN_CREATE_TIME_1, SANGMIN_CREATE_TIME_2)
            self.sangMinStartTime = time.time()
            (sangMinXPos, sangMinYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
            # (플레이어 <-> 상민) 사이 일정한 거리 이상에서 생성되도록
            while ((sangMinXPos - player.xPos) ** 2 + (sangMinYPos - player.yPos) ** 2) ** 0.5 < 300:
                (sangMinXPos, sangMinYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
            sangMin = SangMin(sangMinXPos + SANGMIN_WIDTH / 2, sangMinYPos + SANGMIN_HEIGHT / 2)
            sangMinManager.sangMinList.append(sangMin)

    def init(self):
        self.sangMinLoadTime = 0
        self.sangMinStartTime = time.time()
        self.sangMinList = []
        self.sangMinCreateTime1 = SANGMIN_CREATE_TIME_1
        self.sangMinCreateTime2 = SANGMIN_CREATE_TIME_2