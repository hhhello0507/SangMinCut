import Container
from Container import *
from features.game.setting.SettingFragment import *
from features.game.manager.PlayerManager import *
from src.mysql.DrawManager import *


# TODO: SOUND ON/OFF, CLOSE - 나가기, BACK - 뒤로가기
class GameActivity:
    def init(self):
        container = Container.container
        self.__utils = container["utils"]
        self.__gamePainter = container["gamePainter"]
        self.__gamePainter.init()
        self.__buttonList = self.__gamePainter.getButtonViewList()

    def createBullet(self):
        (xMousePos, yMousePos) = pygame.mouse.get_pos()
        (normalizedXPos, normalizedYPos) = self.__utils.normalized(Player.xPos + PLAYER_WIDTH / 2 - xMousePos,
                                                                   Player.yPos + PLAYER_HEIGHT / 2 - yMousePos)
        bullet = Bullet(Player.xPos + PLAYER_WIDTH / 2, Player.yPos + PLAYER_HEIGHT / 2,
                        -normalizedXPos * BULLET_SPEED,
                        -normalizedYPos * BULLET_SPEED)
        BulletManager.bulletList.append(bullet)

    def onMouseClick(self):
        settingButton = self.__buttonList["settingButton"]
        lifeCycleManager = Container.container["lifeCycleManager"]
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xMousePos, yMousePos) = pygame.mouse.get_pos()
                self.createBullet()
                if settingButton.getXPos() <= xMousePos <= settingButton.getXPos() + settingButton.getWidth() and settingButton.getYPos() <= yMousePos <= settingButton.getYPos() + settingButton.getHeight():
                    lifeCycleManager.isPause = True
                    lifeCycleManager.isSetting = True
                    settingFragment = SettingFragment()
                    settingFragment.startSetting()

    def onKeyClick(self):
        deltaTime = pygame.time.Clock().tick(DEFAULT_FRAME)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if 0 <= Player.xPos - PLAYER_SPEED:
                Player.xPos -= PLAYER_SPEED * deltaTime
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if Player.xPos + PLAYER_SPEED <= SCREEN_WIDTH - PLAYER_WIDTH:
                Player.xPos += PLAYER_SPEED * deltaTime
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if 0 <= Player.yPos - PLAYER_SPEED:
                Player.yPos -= PLAYER_SPEED * deltaTime
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if Player.yPos + PLAYER_SPEED <= SCREEN_HEIGHT - PLAYER_HEIGHT:
                Player.yPos += PLAYER_SPEED * deltaTime
        if keys[pygame.K_SPACE]:
            self.createBullet()
        if keys[pygame.K_r]:
            if Player.isSpecial:
                if not Player.isSpecialing:
                    Player.beforeSpecialTime = time.time()
                    Player.isSpecialing = True
                    Player.playerMaxXp = int(Player.playerMaxXp * 1.2)
                    Player.playerXp = 0

    def startGame(self):
        self.init()
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
        while lifeCycleManager.isPlaying:
            while not lifeCycleManager.isPause:
                # event
                self.onKeyClick()
                self.onMouseClick()
                print("12345")

                bulletManager.manageBullet()
                if STAGES[StageManager.stage][0]: sangMinManager.createSangMin()
                if STAGES[StageManager.stage][1]: galManager.createGal()
                if STAGES[StageManager.stage][2]: hpPotionManager.createHpPotion()
                if STAGES[StageManager.stage][3]: xpPotionManager.createXpPotion()
                if STAGES[StageManager.stage][4]: hoJoonManager.createHojoon()
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