import time

from features.game.pause.PauseFragment import *
from features.game.manager.PlayerManager import *


# TODO: SOUND ON/OFF, CLOSE - 나가기, BACK - 뒤로가기
class GameActivity:
    def init(self):
        container = Container.container
        self.__gamePainter = container["gamePainter"]
        self.__gamePainter.init()
        self.__buttonList = self.__gamePainter.getButtonViewList()

    def createBullet(self):
        from Container import container
        player = container["player"]
        bulletManager = container["bulletManager"]
        (xMousePos, yMousePos) = pygame.mouse.get_pos()
        (normalizedXPos, normalizedYPos) = normalized(player.xPos + PLAYER_WIDTH / 2 - xMousePos,
                                                                   player.yPos + PLAYER_HEIGHT / 2 - yMousePos)
        bullet = Bullet(player.xPos + PLAYER_WIDTH / 2, player.yPos + PLAYER_HEIGHT / 2,
                        -normalizedXPos * BULLET_SPEED,
                        -normalizedYPos * BULLET_SPEED)
        bulletManager.bulletList.append(bullet)

    def onMouseClick(self):
        settingButtonView = self.__buttonList["pauseButtonView"]
        lifeCycleManager = Container.container["lifeCycleManager"]
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.createBullet()
                if settingButtonView.isOnClick(pygame.mouse.get_pos()):
                    lifeCycleManager.isPause = True
                    lifeCycleManager.isPauseFragment = True
                    settingFragment = PauseFragment()
                    settingFragment.startPause()

    def onKeyClick(self):
        from Container import container
        player = container["player"]
        deltaTime = pygame.time.Clock().tick(DEFAULT_FRAME)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if 0 <= player.xPos - PLAYER_SPEED:
                player.xPos -= PLAYER_SPEED * deltaTime
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if player.xPos + PLAYER_SPEED <= SCREEN_WIDTH - PLAYER_WIDTH:
                player.xPos += PLAYER_SPEED * deltaTime
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if 0 <= player.yPos - PLAYER_SPEED:
                player.yPos -= PLAYER_SPEED * deltaTime
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if player.yPos + PLAYER_SPEED <= SCREEN_HEIGHT - PLAYER_HEIGHT:
                player.yPos += PLAYER_SPEED * deltaTime
        if keys[pygame.K_SPACE]:
            self.createBullet()
        if keys[pygame.K_r]:
            if player.isSpecial:
                if not player.isSpecialing:
                    player.beforeSpecialTime = time.time()
                    player.isSpecialing = True
                    player.playerMaxXp = int(player.playerMaxXp * 1.2)
                    player.playerXp = 0
        if keys[pygame.K_ESCAPE]:
            pygame.quit()


    def startGame(self):
        # self.init()
        container = Container.container
        bulletManager = container["bulletManager"]
        sangMinManager = container["sangMinManager"]
        galManager = container["galManager"]
        hpPotionManager = container["hpPotionManager"]
        xpPotionManager = container["xpPotionManager"]
        hoJoonManager = container["hoJoonManager"]
        playerManager = container["playerManager"]
        stageManager = container["stageManager"]
        lifeCycleManager = container["lifeCycleManager"]
        while lifeCycleManager.isGameActivity:
            while not lifeCycleManager.isPause:
                # event
                self.onKeyClick()
                self.onMouseClick()

                bulletManager.manageBullet()
                if STAGES[stageManager.stage][0]: sangMinManager.createSangMin()
                if STAGES[stageManager.stage][1]: galManager.createGal()
                if STAGES[stageManager.stage][2]: hpPotionManager.createHpPotion()
                if STAGES[stageManager.stage][3]: xpPotionManager.createXpPotion()
                if STAGES[stageManager.stage][4]: hoJoonManager.createHojoon()
                hpPotionManager.manageHpPotion()
                playerManager.managePlayer()
                galManager.manageGal()
                sangMinManager.manageSangMin()
                stageManager.manageStage()
                xpPotionManager.manageXpPotion()
                hoJoonManager.manageHojoon()

                # draw
                # DrawManager.drawGame(DrawManager)
                self.__gamePainter.paint()
                self.__gamePainter.update()
                Container.display.update()
                # Container.display.set