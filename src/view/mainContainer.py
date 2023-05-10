from src.model.bullet import *
from src.model.sangmin import *
from src.info.lifeInfo import *
from src.info.clockInfo import *
from src.draw.drawMain import *
from src.draw.drawScene import *
from src.draw.drawSetting import *
import random
import time

# ViewModel
bulletList = []
sangMinList = []

sangMinLoadTime = 0
sangMinStartTime = time.time()


def initPygame():
    global font, mainStartText
    pygame.init()

    font = pygame.font.Font("../res/font/arial.ttf", 30)
    mainStartText = font.render("start", False, (20, 20, 20))

# draw


# view
def onClickStartButton():
    global isMain, isPlaying
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (xMousePos, yMousePos) = pygame.mouse.get_pos()
            if startButton.xPos <= xMousePos <= startButton.xPos + startButton.width and startButton.yPos <= yMousePos <= startButton.yPos + startButton.height:
                isMain = False
                isPlaying = True
        if event.type == pygame.QUIT:
            exit(0)

# view
def onClickSettingButton():
    global isPause, isPlaying
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (xMousePos, yMousePos) = pygame.mouse.get_pos()
            if settingButton.xPos <= xMousePos <= settingButton.xPos + settingButton.width and settingButton.yPos <= yMousePos <= settingButton.yPos + settingButton.height:
                isPause = True
                settingInGame()
        if event.type == pygame.QUIT:
            isPlaying = False

# view
def onClickSoundButton():
    pass
def onClickCloseButton():
    global isPause
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (xMousePos, yMousePos) = pygame.mouse.get_pos()
            if soundButton.xPos <= xMousePos <= soundButton.xPos + soundButton.width and soundButton.yPos <= yMousePos <= soundButton.yPos + soundButton.height:
                print("close")
                isPause = False

# view
def onClickBackButton():
    pass


# TODO: 세팅창 그리기
# TODO: SOUND ON/OFF, CLOSE - 나가기, BACK - 뒤로가기
def settingInGame():
    while isSetting:
        onClickSoundButton()
        onClickCloseButton()
        onClickBackButton()
        drawSetting()


def move():
    deltaTime = clock.tick(60)

    global xPos, yPos
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if 0 <= xPos - PLAYER_SPEED:
            xPos -= PLAYER_SPEED * deltaTime
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if xPos + PLAYER_SPEED <= SCREEN_WIDTH - PLAYER_WIDTH:
            xPos += PLAYER_SPEED * deltaTime
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if 0 <= yPos - PLAYER_SPEED:
            yPos -= PLAYER_SPEED * deltaTime
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if yPos + PLAYER_SPEED <= SCREEN_HEIGHT - PLAYER_HEIGHT:
            yPos += PLAYER_SPEED * deltaTime

# view
def manageBullet():
    for (idx, bullet) in enumerate(bulletList):
        if bullet.isActive:
            bullet.move()
        else:
            bulletList.pop(idx)
# view + viewModel
def createBullet():
    global isPlaying, isPause
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (xMousePos, yMousePos) = pygame.mouse.get_pos()
            (normalizedXPos, normalizedYPos) = normalized(xPos + PLAYER_WIDTH / 2 - xMousePos,
                                                          yPos + PLAYER_HEIGHT / 2 - yMousePos)
            bullet = Bullet(xPos + PLAYER_WIDTH / 2, yPos + PLAYER_HEIGHT / 2, -normalizedXPos * BULLET_SPEED,
                            -normalizedYPos * BULLET_SPEED)
            bulletList.append(bullet)
        if event.type == pygame.QUIT:
            isPause = True
            isPlaying = False

def manageSangMin():
    global playerHP, sangMinList
    activeSangMinList = []
    for (idx, sangMin) in enumerate(sangMinList):
        # 플레이어와 충돌
        if sangMin.objectRect.colliderect(pygame.Rect(xPos, yPos, PLAYER_WIDTH, PLAYER_HEIGHT)):
            sangMin.isActive = False
            playerHP -= 1
            print(playerHP)
        # 총알과 충돌
        for (bulletIdx, bullet) in enumerate(bulletList):
            if sangMin.objectRect.colliderect(bullet.objectRect):
                sangMin.isActive = False
        sangMin.calcMove(xPos + PLAYER_WIDTH / 2, yPos + PLAYER_HEIGHT / 2, SANGMIN_SPEED)
        sangMin.move()
        if sangMin.isActive:
            activeSangMinList.append(sangMin)
    sangMinList = activeSangMinList

# view + viewModel
def createSangMin():
    global sangMinLoadTime, sangMinStartTime, xPos, yPos
    nowTime = time.time()
    if nowTime - sangMinStartTime >= sangMinLoadTime:
        sangMinLoadTime = random.uniform(0.4, 0.7)
        sangMinStartTime = time.time()
        (sangMinXPos, sangMinYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
        while ((sangMinXPos - xPos) ** 2 + (sangMinYPos - yPos) ** 2) ** 0.5 < 300:
            (sangMinXPos, sangMinYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
        sangMin = SangMin(sangMinXPos + SANGMIN_WIDTH / 2, sangMinYPos + SANGMIN_HEIGHT / 2)
        sangMinList.append(sangMin)


def main():
    initPygame()
    drawMain()
    while isMain:
        onClickStartButton()
    while isPlaying:
        while not isPause:
            manageBullet()
            createBullet()
            manageSangMin()
            createSangMin()
            onClickSettingButton()
            move()
            drawScene()
    pygame.quit()