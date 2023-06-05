import time

from src.entity.Player import *
from src.entity.XpPotion import *


class XpPotionManager:

    def __init__(self):
        self.xpPotionList = []
        self.xpLoadTime = 0
        self.xpStartTime = time.time()

    def createXpPotion(self):
        from Container import container
        player = container["player"]
        now = time.time()
        if now - self.xpStartTime > self.xpLoadTime:
            self.xpStartTime = now
            self.xpLoadTime = random.uniform(XP_CREATE_TIME_1, XP_CREATE_TIME_2)
            (xpPotionXPos, xpPotionYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
            # (플레이어 <-> mp포션) 사이 일정한 거리 이상에서 생성되도록
            while ((xpPotionXPos - player.xPos) ** 2 + (xpPotionYPos - player.yPos) ** 2) ** 0.5 < 300:
                (xpPotionXPos, xpPotionYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
            xpPotion = XpPotion(xpPotionXPos + XP_POTION_WIDTH / 2, xpPotionYPos + XP_POTION_HEIGHT / 2)
            self.xpPotionList.append(xpPotion)

    def manageXpPotion(self):
        from Container import container
        player = container["player"]
        activeXpPotionList = []
        for (idx, xpPotion) in enumerate(self.xpPotionList):
            # 플레이어와 충돌
            if xpPotion.objectRect.colliderect(pygame.Rect(player.xPos, player.yPos, PLAYER_WIDTH, PLAYER_HEIGHT)):
                xpPotion.isActive = False
                player.playerXp += xpPotion.xp
                print("PlayerXP : +%d" % (player.playerXp))
            if xpPotion.isActive:
                activeXpPotionList.append(xpPotion)
        self.xpPotionList = activeXpPotionList

    def init(self):
        self.xpPotionList.clear()
        self.xpLoadTime = 0
        self.xpStartTime = time.time()
