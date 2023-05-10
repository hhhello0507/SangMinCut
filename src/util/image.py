import pygame
from src.util.constants import *

IMG_BACKGROUND = pygame.image.load("../res/image/background.jpg")
IMG_BACKGROUND = pygame.transform.scale(IMG_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

IMG_PLAYER = pygame.image.load("../res/image/player1.png")
IMG_PLAYER = pygame.transform.scale(IMG_PLAYER, (PLAYER_WIDTH, PLAYER_HEIGHT))

IMG_BULLET = pygame.image.load("../res/image/bullet.png")
IMG_BULLET = pygame.transform.scale(IMG_BULLET, (BULLET_WIDTH, BULLET_HEIGHT))
