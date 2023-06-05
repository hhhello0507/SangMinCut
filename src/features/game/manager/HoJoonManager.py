from src.entity.Hojoon import *
from src.entity.Player import *
from features.game.manager.BulletManager import *
import time
import random
import math

class HoJoonManager:

    def __init__(self):
        self.hojoonList = []
        self.hojoonTime = 0
        self.hojoonStartTime = time.time()

    def manageHojoon(self):
        from Container import container
        activeHojoonList = []
        player = container["player"]
        bulletManager = container["bulletManager"]
        for (idx, hojoon) in enumerate(self.hojoonList):
            if not isObjectInMap(hojoon):
                hojoon.isActive = False
            # 플레이어와 충돌
            if hojoon.objectRect.colliderect(pygame.Rect(player.xPos, player.yPos, PLAYER_WIDTH, PLAYER_HEIGHT)):
                hojoon.isActive = False
                player.playerHp -= 1.5
                print("PlayerHP : -%d" % (player.playerHp))
            # 총알과 충돌
            for (bulletIdx, bullet) in enumerate(bulletManager.bulletList):
                if hojoon.objectRect.colliderect(bullet.objectRect):
                    hojoon.isActive = False
                    player.playerXp += 1.5
                    print("playerXP : +%d" % player.playerXp)
            hojoon.move()
            hojoon.yPos = (math.sin(hojoon.a * hojoon.xPos) + math.sin(hojoon.b * hojoon.xPos) + math.sin(hojoon.c * hojoon.xPos)) * 30 + hojoon.h
            # print(hojoon.xPos, hojoon.yPos)
            if hojoon.isActive:
                activeHojoonList.append(hojoon)
                self.hojoonList = activeHojoonList
        self.hojoonList = activeHojoonList

    def createHojoon(self):
        now = time.time()
        if now - self.hojoonStartTime >= self.hojoonTime:
            self.hojoonTime = random.uniform(GAL_CREATE_TIME_1, GAL_CREATE_TIME_2)
            self.hojoonStartTime = time.time()
            hojoon = Hojoon(0, 0)
            if random.randint(0, 1):
                hojoon.xPos = 0
                hojoon.xMove = HOJOON_SPEED
            else:
                hojoon.xPos = SCREEN_WIDTH - 50
                hojoon.xMove = -HOJOON_SPEED
            setHojoonThreeSin(hojoon)
            self.hojoonList.append(hojoon)
    def init(self):
        self.hojoonList.clear()
        self.hojoonTime = 0
        self.hojoonStartTime = time.time()
