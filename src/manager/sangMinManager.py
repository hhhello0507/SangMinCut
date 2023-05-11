import pygame
from src.entity.player import *
from src.manager.bulletManager import *
class SangMinManager:
    sangMinList = []
    def manageSangMin(self):
        activeSangMinList = []
        for (idx, sangMin) in enumerate(self.sangMinList):
            # 플레이어와 충돌
            if sangMin.objectRect.colliderect(pygame.Rect(Player.xPos, Player.yPos, PLAYER_WIDTH, PLAYER_HEIGHT)):
                sangMin.isActive = False
                Player.playerHP -= 1
                print(Player.playerHP)
            # 총알과 충돌
            for (bulletIdx, bullet) in enumerate(BulletManager.bulletList):
                if sangMin.objectRect.colliderect(bullet.objectRect):
                    sangMin.isActive = False
            sangMin.calcMove(Player.xPos + PLAYER_WIDTH / 2, Player.yPos + PLAYER_HEIGHT / 2, SANGMIN_SPEED)
            sangMin.move()
            if sangMin.isActive:
                activeSangMinList.append(sangMin)
        self.sangMinList = activeSangMinList