import pygame
from src.util.image import *
from src.util.constants import *
from src.util.utils import *
from src.bullet import *
import random

isPlaying = True

display = pygame.display

clock = pygame.time.Clock()

xPos = (SCREEN_WIDTH - PLAYER_WIDTH) / 2
yPos = (SCREEN_HEIGHT - PLAYER_HEIGHT) / 2
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bulletList = []

def init():
    global screen
    pygame.init()
    display.set_caption("My game")


def draw():
    screen.blit(IMG_BACKGROUND, (0, 0))
    screen.blit(IMG_PLAYER, (xPos, yPos))
    for bullet in bulletList:
        screen.blit(IMG_BULLET, (bullet.xPos, bullet.yPos))
    display.update()


def main():
    global isPlaying, xPos, yPos
    init()
    while isPlaying:
        for (idx, bullet) in enumerate(bulletList):
            if bullet.isActive:
                bullet.move()
            else:
                bulletList.pop(idx)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xMousePos, yMousePos) = pygame.mouse.get_pos()
                (normalizedXPos, normalizedYPos) = normalized(xPos + PLAYER_WIDTH / 2 - xMousePos, yPos + PLAYER_HEIGHT / 2 - yMousePos)
                bullet = Bullet(xPos + PLAYER_WIDTH / 2, yPos + PLAYER_HEIGHT / 2, -normalizedXPos * BULLET_SPEED, -normalizedYPos * BULLET_SPEED)
                bulletList.append(bullet)
            if event.type == pygame.QUIT:
                isPlaying = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if 0 <= xPos - PLAYER_SPEED <= SCREEN_WIDTH:
                xPos -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            if 0 <= xPos + PLAYER_SPEED <= SCREEN_WIDTH - PLAYER_WIDTH:
                xPos += PLAYER_SPEED
        if keys[pygame.K_UP]:
            if 0 <= yPos - PLAYER_SPEED <= SCREEN_HEIGHT:
                yPos -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            if 0 <= yPos + PLAYER_SPEED <= SCREEN_HEIGHT - PLAYER_HEIGHT:
                yPos += PLAYER_SPEED
        draw()
    pygame.quit()


main()
