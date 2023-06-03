import time
from src.entity.Player import *
from src.entity.XpPotion import *


class XpPotionManager:
    xpPotionList = []
    xpLoadTime = 0
    xpStartTime = time.time()

    def createXpPotion(self):
        now = time.time()
        if now - self.xpStartTime > self.xpLoadTime:
            self.xpStartTime = now
            self.xpLoadTime = random.uniform(XP_CREATE_TIME_1, XP_CREATE_TIME_2)
            (xpPotionXPos, xpPotionYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
            # (플레이어 <-> mp포션) 사이 일정한 거리 이상에서 생성되도록
            while ((xpPotionXPos - Player.xPos) ** 2 + (xpPotionYPos - Player.yPos) ** 2) ** 0.5 < 300:
                (xpPotionXPos, xpPotionYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
            xpPotion = XpPotion(xpPotionXPos + XP_POTION_WIDTH / 2, xpPotionYPos + XP_POTION_HEIGHT / 2)
            self.xpPotionList.append(xpPotion)

    def manageXpPotion(self):
        activeXpPotionList = []
        for (idx, xpPotion) in enumerate(self.xpPotionList):
            # 플레이어와 충돌
            if xpPotion.objectRect.colliderect(pygame.Rect(Player.xPos, Player.yPos, PLAYER_WIDTH, PLAYER_HEIGHT)):
                xpPotion.isActive = False
                Player.playerXp += xpPotion.xp
                print("PlayerXP : +%d" % (Player.playerXp))
            if xpPotion.isActive:
                activeXpPotionList.append(xpPotion)
        self.xpPotionList = activeXpPotionList
