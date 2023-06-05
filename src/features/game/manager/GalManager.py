from src.entity.Gal import *
from src.entity.Player import *
from features.game.manager.BulletManager import *
import time
import random

class GalManager:

    def __init__(self):
        self.galList = []
        self.galLoadTime = 0
        self.galStartTime = time.time()


    def manageGal(self):
        from Container import container
        player = container["player"]
        bulletManager = container["bulletManager"]
        activeGalList = []
        for (idx, gal) in enumerate(self.galList):
            if not isObjectInMap(gal):
                gal.isActive = False
            # 플레이어와 충돌
            if gal.objectRect.colliderect(pygame.Rect(player.xPos, player.yPos, PLAYER_WIDTH, PLAYER_HEIGHT)):
                gal.isActive = False
                player.playerHp -= 1
                print("PlayerHP : -%d" % (player.playerHp))
        # 총알과 충돌
            for (bulletIdx, bullet) in enumerate(bulletManager.bulletList):
                if gal.objectRect.colliderect(bullet.objectRect):
                    gal.isActive = False
                    player.playerXp += 1
                    print("playerXP : +%d" % player.playerXp)
            gal.move()
            gal.yPos = gal.a * (gal.xPos - gal.s) ** 2 + gal.h
            if gal.isActive:
                activeGalList.append(gal)
                self.galList = activeGalList
            if gal.yPos > SCREEN_HEIGHT:
                setGalQuadraticGraph(gal)
                gal.yPos = SCREEN_HEIGHT - 10
        self.galList = activeGalList

    def createGal(self):
        now = time.time()
        if now - self.galStartTime >= self.galLoadTime:
            self.galLoadTime = random.uniform(GAL_CREATE_TIME_1, GAL_CREATE_TIME_2)
            self.galStartTime = time.time()
            gal = Gal(0, SCREEN_HEIGHT)
            if random.randint(0, 1):
                gal.d = True
                gal.xPos = 0
                gal.xMove = GAL_SPEED
            else:
                gal.d = False
                gal.xPos = SCREEN_WIDTH - 50
                gal.xMove = -GAL_SPEED
            setGalQuadraticGraph(gal)

            # print(gal.a, gal.s, gal.h)
            self.galList.append(gal)

    def init(self):
        self.galList.clear()
        self.galLoadTime = 0
        self.galStartTime = time.time()