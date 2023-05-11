from src.entity.bullet import *
from src.info.clockInfo import *
from src.view.settingFragment import *
from src.manager.drawManager import *
from src.manager.bulletManager import *
from src.manager.sangMinManager import *
from src.info.drawInfo import *
from src.entity.player import *


# TODO: 세팅창 그리기
# TODO: SOUND ON/OFF, CLOSE - 나가기, BACK - 뒤로가기

class GameActivity:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.data = data
            cls._init = True

    def createBullet(self):
        (xMousePos, yMousePos) = pygame.mouse.get_pos()
        (normalizedXPos, normalizedYPos) = normalized(Player.xPos + PLAYER_WIDTH / 2 - xMousePos,
                                                      Player.yPos + PLAYER_HEIGHT / 2 - yMousePos)
        bullet = Bullet(Player.xPos + PLAYER_WIDTH / 2, Player.yPos + PLAYER_HEIGHT / 2,
                        -normalizedXPos * BULLET_SPEED,
                        -normalizedYPos * BULLET_SPEED)
        BulletManager.bulletList.append(bullet)


    def onMouseClick(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xMousePos, yMousePos) = pygame.mouse.get_pos()
                self.createBullet(self)
                if DrawInfo.settingButton.xPos <= xMousePos <= DrawInfo.settingButton.xPos + DrawInfo.settingButton.width and DrawInfo.settingButton.yPos <= yMousePos <= DrawInfo.settingButton.yPos + DrawInfo.settingButton.height:
                    LifeInfo.isPause = True
                    LifeInfo.isSetting = True
                    settingFragment()


    def onKeyClick(self):
        # move
        deltaTime = clock.tick(60)
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
    def startGame(self):
        while LifeInfo.isPlaying:
            while not LifeInfo.isPause:
                # event
                self.onKeyClick(self)
                self.onMouseClick(self)

                # manage
                BulletManager.manageBullet(BulletManager)
                SangMinManager.manageSangMin(SangMinManager)
                SangMinManager.createSangMin(SangMinManager)

                # draw
                DrawManager.drawGame(DrawManager)