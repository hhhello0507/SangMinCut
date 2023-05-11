from src.entity.bullet import *
from src.entity.sangmin import *
from src.info.lifeInfo import *
from src.info.clockInfo import *
from src.draw.drawMain import *
from src.draw.drawScene import *
from src.draw.drawSetting import *
from src.info.drawInfo import *
from src.manager.bulletManager import *
from src.manager.sangMinManager import *
from src.entity.player import *
import random
import time


# TODO: 세팅창 그리기
# TODO: SOUND ON/OFF, CLOSE - 나가기, BACK - 뒤로가기

bulletManager = BulletManager
sangMinManager = SangMinManager

sangMinLoadTime = 0
sangMinStartTime = time.time()

# view + viewModel
def createSangMin():
    global sangMinLoadTime, sangMinStartTime
    nowTime = time.time()
    if nowTime - sangMinStartTime >= sangMinLoadTime:
        sangMinLoadTime = random.uniform(0.4, 0.7)
        sangMinStartTime = time.time()
        (sangMinXPos, sangMinYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
        while ((sangMinXPos - Player.xPos) ** 2 + (sangMinYPos - Player.yPos) ** 2) ** 0.5 < 300:
            (sangMinXPos, sangMinYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
        sangMin = SangMin(sangMinXPos + SANGMIN_WIDTH / 2, sangMinYPos + SANGMIN_HEIGHT / 2)
        SangMinManager.sangMinList.append(sangMin)

def onMouseClick():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (xMousePos, yMousePos) = pygame.mouse.get_pos()
            (normalizedXPos, normalizedYPos) = normalized(Player.xPos + PLAYER_WIDTH / 2 - xMousePos,
                                                          Player.yPos + PLAYER_HEIGHT / 2 - yMousePos)
            bullet = Bullet(Player.xPos + PLAYER_WIDTH / 2, Player.yPos + PLAYER_HEIGHT / 2,
                            -normalizedXPos * BULLET_SPEED,
                            -normalizedYPos * BULLET_SPEED)
            BulletManager.bulletList.append(bullet)
            if DrawInfo.settingButton.xPos <= xMousePos <= DrawInfo.settingButton.xPos + DrawInfo.settingButton.width and DrawInfo.settingButton.yPos <= yMousePos <= DrawInfo.settingButton.yPos + DrawInfo.settingButton.height:
                LifeInfo.isPause = True
                LifeInfo.isSetting = True
                settingInGame()

def settingInGame():
    while LifeInfo.isSetting:
        # TODO: onClickSoundButton()
        # TODO: onClickBackButton()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xMousePos, yMousePos) = pygame.mouse.get_pos()
                if DrawInfo.soundButton.xPos <= xMousePos <= DrawInfo.soundButton.xPos + DrawInfo.soundButton.width and DrawInfo.soundButton.yPos <= yMousePos <= DrawInfo.soundButton.yPos + DrawInfo.soundButton.height:
                    LifeInfo.isSetting = False
                    LifeInfo.isPause = False
            if event.type == pygame.QUIT:
                pygame.quit()
        drawSetting()
def onKeyClick():
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
def gameStart():
    while LifeInfo.isPlaying:
        while not LifeInfo.isPause:
            # event
            onKeyClick()
            onMouseClick()

            # manage
            createSangMin()
            bulletManager.manageBullet(bulletManager)
            sangMinManager.manageSangMin(sangMinManager)

            # draw
            drawScene()