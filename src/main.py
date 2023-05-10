import pygame
from src.util.image import *
from src.util.utils import *
from src.bullet import *
from src.sangmin import *
import random
import time

isPlaying = True

display = pygame.display

clock = pygame.time.Clock()

xPos = (SCREEN_WIDTH - PLAYER_WIDTH) / 2
yPos = (SCREEN_HEIGHT - PLAYER_HEIGHT) / 2
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bulletList = []
sangMinList = []

sangMinLoadTime = 0
sangMinStartTime = time.time()
sangMinDeltaTime = 0

def init():
    global screen
    pygame.init()
    display.set_caption("My game")


def draw():
    screen.blit(IMG_BACKGROUND, (0, 0))
    screen.blit(IMG_PLAYER, (xPos, yPos))
    for bullet in bulletList:
        screen.blit(IMG_BULLET, (bullet.xPos, bullet.yPos))
    for sangMin in sangMinList:
        screen.blit(IMG_SANGMIN, (sangMin.xPos, sangMin.yPos))
    display.update()

def move():
    global xPos, yPos
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if 0 <= xPos - PLAYER_SPEED <= SCREEN_WIDTH:
            xPos -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if 0 <= xPos + PLAYER_SPEED <= SCREEN_WIDTH - PLAYER_WIDTH:
            xPos += PLAYER_SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if 0 <= yPos - PLAYER_SPEED <= SCREEN_HEIGHT:
            yPos -= PLAYER_SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if 0 <= yPos + PLAYER_SPEED <= SCREEN_HEIGHT - PLAYER_HEIGHT:
            yPos += PLAYER_SPEED

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
    for (idx, sangMin) in enumerate(sangMinList):
        if sangMin.isActive:
            sangMin.calcMove(xPos + PLAYER_WIDTH / 2, yPos + PLAYER_HEIGHT / 2, SANGMIN_SPEED)
            sangMin.move()
        else:
            sangMinList.pop(idx)

def createSangMin():
    global sangMinLoadTime, sangMinStartTime
    nowTime = time.time()
    if nowTime - sangMinStartTime >= sangMinLoadTime:
        sangMinLoadTime = random.uniform(0, 0.01)
        sangMinStartTime = time.time()
        (xPos, yPos) = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
        sangMin = SangMin(xPos + SANGMIN_WIDTH / 2, yPos + SANGMIN_HEIGHT / 2)
        sangMinList.append(sangMin)

    # print(sangMinLoadTime)

def main():
    init()
    while isPlaying:
        manageBullet()
        createBullet()
        manageSangMin()
        createSangMin()
        move()
        draw()
    pygame.quit()


main()
