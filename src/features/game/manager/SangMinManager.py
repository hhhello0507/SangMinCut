from src.entity.Player import *
from features.game.manager.BulletManager import *
from src.entity.Sangmin import *
import time
import random

class SangMinManager:
    sangMinLoadTime = 0
    sangMinStartTime = time.time()
    sangMinList = []
    sangMinCreateTime1 = SANGMIN_CREATE_TIME_1
    sangMinCreateTime2 = SANGMIN_CREATE_TIME_2


    def manageSangMin(self):
        activeSangMinList = []
        for (idx, sangMin) in enumerate(SangMinManager.sangMinList):
            if not isObjectInMap(sangMin):
                sangMin.isActive = False
            # 플레이어와 충돌
            if sangMin.objectRect.colliderect(pygame.Rect(Player.xPos, Player.yPos, PLAYER_WIDTH, PLAYER_HEIGHT)):
                sangMin.isActive = False
                Player.playerHp -= 1
                print("PlayerHP : -%d" % (Player.playerHp))
            # 총알과 충돌
            for (bulletIdx, bullet) in enumerate(BulletManager.bulletList):
                if sangMin.objectRect.colliderect(bullet.objectRect):
                    sangMin.isActive = False
                    Player.playerXp += 1
                    print("playerXP : +%d" % Player.playerXp)
            sangMin.calcMove(Player.xPos + PLAYER_WIDTH / 2, Player.yPos + PLAYER_HEIGHT / 2, SANGMIN_SPEED)
            sangMin.move()
            if sangMin.isActive:
                activeSangMinList.append(sangMin)
        SangMinManager.sangMinList = activeSangMinList

    def createSangMin(self):
        nowTime = time.time()
        if nowTime - SangMinManager.sangMinStartTime >= SangMinManager.sangMinLoadTime:
            SangMinManager.sangMinLoadTime = random.uniform(SANGMIN_CREATE_TIME_1, SANGMIN_CREATE_TIME_2)
            SangMinManager.sangMinStartTime = time.time()
            (sangMinXPos, sangMinYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
            # (플레이어 <-> 상민) 사이 일정한 거리 이상에서 생성되도록
            while ((sangMinXPos - Player.xPos) ** 2 + (sangMinYPos - Player.yPos) ** 2) ** 0.5 < 300:
                (sangMinXPos, sangMinYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
            sangMin = SangMin(sangMinXPos + SANGMIN_WIDTH / 2, sangMinYPos + SANGMIN_HEIGHT / 2)
            SangMinManager.sangMinList.append(sangMin)

def sangMinInit():
    SangMinManager.sangMinLoadTime = 0
    SangMinManager.sangMinStartTime = time.time()
    SangMinManager.sangMinList = []
    SangMinManager.sangMinCreateTime1 = SANGMIN_CREATE_TIME_1
    SangMinManager.sangMinCreateTime2 = SANGMIN_CREATE_TIME_2