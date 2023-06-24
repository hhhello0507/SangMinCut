import random
import time

import Container
from src.entity.HpPotion import *
from src.entity.Player import *


class HpPotionManager:
    def __init__(self):
        self.hpPotionList = []
        self.hpLoadTime = 0
        self.hpStartTime = time.time()

    def createHpPotion(self):
        player = Container.container["player"]
        now = time.time()
        if now - self.hpStartTime > self.hpLoadTime:
            self.hpStartTime = now
            self.hpLoadTime = random.uniform(HP_CREATE_TIME_1, HP_CREATE_TIME_2)
            (hpPotionXPos, hpPotionYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
            # (플레이어 <-> hp포션) 사이 일정한 거리 이상에서 생성되도록
            while ((hpPotionXPos - player.xPos) ** 2 + (hpPotionYPos - player.yPos) ** 2) ** 0.5 < 300:
                (hpPotionXPos, hpPotionYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
            hpPotion = HpPotion(hpPotionXPos + HP_POTION_WIDTH / 2, hpPotionYPos + HP_POTION_HEIGHT / 2)
            self.hpPotionList.append(hpPotion)

    def manageHpPotion(self):
        player = Container.container["player"]
        activeHpPotionList = []
        for (idx, hpPotion) in enumerate(self.hpPotionList):
            # 플레이어와 충돌
            if hpPotion.objectRect.colliderect(pygame.Rect(player.xPos, player.yPos, PLAYER_WIDTH, PLAYER_HEIGHT)):
                hpPotion.isActive = False
                player.playerHp += hpPotion.hp
                print("PlayerHP : +%d" % (player.playerHp))
            if hpPotion.isActive:
                activeHpPotionList.append(hpPotion)
        self.hpPotionList = activeHpPotionList

    def init(self):
        self.hpPotionList.clear()
        self.hpStartTime = 0
        self.hpStartTime = time.time()