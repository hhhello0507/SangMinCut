from src.entity.bullet import *
from src.info.clockInfo import *
from src.draw.drawGame import *
from src.view.settingFragment import *
from src.info.drawInfo import *
from src.entity.player import *


# TODO: 세팅창 그리기
# TODO: SOUND ON/OFF, CLOSE - 나가기, BACK - 뒤로가기

bulletManager = BulletManager
sangMinManager = SangMinManager


def createBullet():
    (xMousePos, yMousePos) = pygame.mouse.get_pos()
    (normalizedXPos, normalizedYPos) = normalized(Player.xPos + PLAYER_WIDTH / 2 - xMousePos,
                                                  Player.yPos + PLAYER_HEIGHT / 2 - yMousePos)
    bullet = Bullet(Player.xPos + PLAYER_WIDTH / 2, Player.yPos + PLAYER_HEIGHT / 2,
                    -normalizedXPos * BULLET_SPEED,
                    -normalizedYPos * BULLET_SPEED)
    BulletManager.bulletList.append(bullet)


def onMouseClick():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (xMousePos, yMousePos) = pygame.mouse.get_pos()
            createBullet()
            if DrawInfo.settingButton.xPos <= xMousePos <= DrawInfo.settingButton.xPos + DrawInfo.settingButton.width and DrawInfo.settingButton.yPos <= yMousePos <= DrawInfo.settingButton.yPos + DrawInfo.settingButton.height:
                LifeInfo.isPause = True
                LifeInfo.isSetting = True
                settingFragment()


def onKeyClick():
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
def startGame():
    while LifeInfo.isPlaying:
        while not LifeInfo.isPause:
            # event
            onKeyClick()
            onMouseClick()

            # manage
            bulletManager.manageBullet(bulletManager)
            sangMinManager.manageSangMin(sangMinManager)
            sangMinManager.createSangMin(sangMinManager)

            # draw
            drawGame()