import pygame
from src.entity.Player import *
from src.manager.BulletManager import *
from src.entity.Sangmin import *
import time
import random

class SangMinManager:
    sangMinLoadTime = 0
    sangMinStartTime = time.time()
    sangMinList = []
    sangMinCreateTime1 = SANGMIN_CREATE_TIME_1
    sangMinCreateTime2 = SANGMIN_CREATE_TIME_2

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.data = data
            cls._init = True
    def manageSangMin(self):
        activeSangMinList = []
        for (idx, sangMin) in enumerate(self.sangMinList):
            # 플레이어와 충돌
            if sangMin.objectRect.colliderect(pygame.Rect(Player.xPos, Player.yPos, PLAYER_WIDTH, PLAYER_HEIGHT)):
                sangMin.isActive = False
                Player.playerHP -= 1
                print("PlayerHP - %d" %(Player.playerHP))
            # 총알과 충돌
            for (bulletIdx, bullet) in enumerate(BulletManager.bulletList):
                if sangMin.objectRect.colliderect(bullet.objectRect):
                    sangMin.isActive = False
                    Player.playerXP += 1
                    print("playerXP - %d" %Player.playerXP)
            sangMin.calcMove(Player.xPos + PLAYER_WIDTH / 2, Player.yPos + PLAYER_HEIGHT / 2, SANGMIN_SPEED)
            sangMin.move()
            if sangMin.isActive:
                activeSangMinList.append(sangMin)
        self.sangMinList = activeSangMinList

    def createSangMin(self):
        nowTime = time.time()
        if nowTime - self.sangMinStartTime >= self.sangMinLoadTime:
            self.sangMinLoadTime = random.uniform(SANGMIN_CREATE_TIME_1, SANGMIN_CREATE_TIME_2)
            self.sangMinStartTime = time.time()
            (sangMinXPos, sangMinYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
            # (플레이어 <-> 상민) 사이 일정한 거리 이상에서 생성되도록
            while ((sangMinXPos - Player.xPos) ** 2 + (sangMinYPos - Player.yPos) ** 2) ** 0.5 < 300:
                (sangMinXPos, sangMinYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
            sangMin = SangMin(sangMinXPos + SANGMIN_WIDTH / 2, sangMinYPos + SANGMIN_HEIGHT / 2)
            SangMinManager.sangMinList.append(sangMin)
