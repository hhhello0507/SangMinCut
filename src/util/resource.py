import pygame
from src.util.constants import *

IMG_BACKGROUND = pygame.image.load("../res/image/background.jpg")
IMG_BACKGROUND = pygame.transform.scale(IMG_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

IMG_PLAYER = pygame.image.load("../res/image/sangmin2.png")
IMG_PLAYER = pygame.transform.scale(IMG_PLAYER, (PLAYER_WIDTH, PLAYER_HEIGHT))

IMG_BULLET = pygame.image.load("../res/image/sangmin2.png")
IMG_BULLET = pygame.transform.scale(IMG_BULLET, (BULLET_WIDTH, BULLET_HEIGHT))

IMG_SANGMIN = pygame.image.load("../res/image/sangmin2.png")
IMG_SANGMIN = pygame.transform.scale(IMG_SANGMIN, (SANGMIN_WIDTH, SANGMIN_HEIGHT))

IMG_BUTTON = pygame.image.load("../res/image/bullet.png")
IMG_BUTTON = pygame.transform.scale(IMG_BUTTON, (BUTTON_WIDTH, BUTTON_HEIGHT))

IMG_SETTING = pygame.image.load("../res/image/bullet.png")
IMG_SETTING = pygame.transform.scale(IMG_SETTING, (SETTING_WIDTH, SETTING_HEIGHT))

#
IMG_SOUND_BUTTON = pygame.image.load("../res/image/bullet.png")
IMG_SOUND_BUTTON = pygame.transform.scale(IMG_SOUND_BUTTON, (SOUND_BUTTON_WIDTH, SOUND_BUTTON_HEIGHT))

IMG_CLOSE_BUTTON = pygame.image.load("../res/image/bullet.png")
IMG_CLOSE_BUTTON = pygame.transform.scale(IMG_CLOSE_BUTTON, (CLOSE_BUTTON_WIDTH, CLOSE_BUTTON_HEIGHT))

IMG_BACK_BUTTON = pygame.image.load("../res/image/bullet.png")
IMG_BACK_BUTTON = pygame.transform.scale(IMG_BACK_BUTTON, (BACK_BUTTON_WIDTH, BACK_BUTTON_HEIGHT))