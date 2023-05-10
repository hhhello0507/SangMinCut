import pygame
from src.util.resource import *
from src.util.utils import *
from src.bullet import *
from src.sangmin import *
from src.button import *

import random
import time

clock = pygame.time.Clock()

isPlaying = True
isMain = True

display = pygame.display

playerHp = 10
xPos = (SCREEN_WIDTH - PLAYER_WIDTH) / 2
yPos = (SCREEN_HEIGHT - PLAYER_HEIGHT) / 2
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bulletList = []
sangMinList = []

sangMinLoadTime = 0
sangMinStartTime = time.time()

startButton = Button(SCREEN_WIDTH - BUTTON_WIDTH, SCREEN_HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)

font = 0
mainStartText = 0


def init():
    global screen, font, mainStartText
    pygame.init()
    display.set_caption("My game")

    font = pygame.font.Font("../res/font/arial.ttf", 30)
    mainStartText = font.render("start", False, (20, 20, 20))

def drawMain():
    screen.blit(IMG_BUTTON, (startButton.xPos, startButton.yPos))
    screen.blit(mainStartText, (startButton.xPos + 40, startButton.yPos + 20))
    display.update()

def drawGame():
    screen.blit(IMG_BACKGROUND, (0, 0))
    screen.blit(IMG_PLAYER, (xPos, yPos))
    for bullet in bulletList:
        screen.blit(IMG_BULLET, (bullet.xPos, bullet.yPos))
    for sangMin in sangMinList:
        screen.blit(IMG_SANGMIN, (sangMin.xPos, sangMin.yPos))
    display.update()

def observeOnClickButton():
    global isMain
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (xMousePos, yMousePos) = pygame.mouse.get_pos()
            if startButton.xPos <= xMousePos <= startButton.xPos + startButton.width and startButton.yPos <= yMousePos <= startButton.yPos + startButton.height:
                isMain = False
        if event.type == pygame.QUIT:
            exit(0)

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

def manageBullet():
    for (idx, bullet) in enumerate(bulletList):
        if bullet.isActive:
            bullet.move()
        else:
            bulletList.pop(idx)

def createBullet():
    global isPlaying
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (xMousePos, yMousePos) = pygame.mouse.get_pos()
            (normalizedXPos, normalizedYPos) = normalized(xPos + PLAYER_WIDTH / 2 - xMousePos,
                                                          yPos + PLAYER_HEIGHT / 2 - yMousePos)
            bullet = Bullet(xPos + PLAYER_WIDTH / 2, yPos + PLAYER_HEIGHT / 2, -normalizedXPos * BULLET_SPEED,
                            -normalizedYPos * BULLET_SPEED)
            bulletList.append(bullet)
        if event.type == pygame.QUIT:
            isPlaying = False
def manageSangMin():
    global playerHp, sangMinList
    activeSangMinList = []
    for (idx, sangMin) in enumerate(sangMinList):
        # 플레이어와 충돌
        if sangMin.objectRect.colliderect(pygame.Rect(xPos, yPos, PLAYER_WIDTH, PLAYER_HEIGHT)):
            sangMin.isActive = False
            playerHp -= 1
            print(playerHp)
        # 총알과 충돌
        for (bulletIdx, bullet) in enumerate(bulletList):
            if sangMin.objectRect.colliderect(bullet.objectRect):
                sangMin.isActive = False
        sangMin.calcMove(xPos + PLAYER_WIDTH / 2, yPos + PLAYER_HEIGHT / 2, SANGMIN_SPEED)
        sangMin.move()
        if sangMin.isActive:
            activeSangMinList.append(sangMin)
    sangMinList = activeSangMinList


def createSangMin():
    global sangMinLoadTime, sangMinStartTime, xPos, yPos
    nowTime = time.time()
    if nowTime - sangMinStartTime >= sangMinLoadTime:
        sangMinLoadTime = random.uniform(0.4, 0.7)
        sangMinStartTime = time.time()
        # TODO: 플레이어로부터 n거리 만큼 떨어지도록
        (sangMinXPos, sangMinYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
        while ((sangMinXPos - xPos) ** 2 + (sangMinYPos - yPos) ** 2) ** 0.5 < 300:
            (sangMinXPos, sangMinYPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
        sangMin = SangMin(sangMinXPos + SANGMIN_WIDTH / 2, sangMinYPos + SANGMIN_HEIGHT / 2)
        sangMinList.append(sangMin)

def main():
    init()
    drawMain()
    while isMain:
        observeOnClickButton()
    while isPlaying:
        manageBullet()
        createBullet()
        manageSangMin()
        createSangMin()
        move()
        drawGame()
    pygame.quit()


main()
