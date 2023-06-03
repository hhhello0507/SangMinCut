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

IMG_GAL = pygame.image.load("../res/image/sangmin3.jpg")
IMG_GAL = pygame.transform.scale(IMG_GAL, (GAL_WIDTH, GAL_HEIGHT))

IMG_HOJOON = pygame.image.load("../res/image/hojoon.png")
IMG_HOJOON = pygame.transform.scale(IMG_HOJOON, (HOJOON_WIDTH, HOJOON_HEIGHT))

IMG_HP_POTION = pygame.image.load("../res/image/player1.png")
IMG_HP_POTION = pygame.transform.scale(IMG_HP_POTION, (HP_POTION_WIDTH, HP_POTION_HEIGHT))

IMG_XP_POTION = pygame.image.load("../res/image/player1.png")
IMG_XP_POTION = pygame.transform.scale(IMG_XP_POTION, (XP_POTION_WIDTH, XP_POTION_HEIGHT))

IMG_SETTING_BUTTON = pygame.image.load("../res/image/bullet.png")
IMG_SETTING_BUTTON = pygame.transform.scale(IMG_SETTING_BUTTON, (SETTING_BUTTON_WIDTH, SETTING_BUTTON_HEIGHT))

IMG_SOUND_BUTTON = pygame.image.load("../res/image/bullet.png")
IMG_SOUND_BUTTON = pygame.transform.scale(IMG_SOUND_BUTTON, (SOUND_BUTTON_WIDTH, SOUND_BUTTON_HEIGHT))

IMG_CLOSE_BUTTON = pygame.image.load("../res/image/bullet.png")
IMG_CLOSE_BUTTON = pygame.transform.scale(IMG_CLOSE_BUTTON, (CLOSE_BUTTON_WIDTH, CLOSE_BUTTON_HEIGHT))

IMG_BACK_BUTTON = pygame.image.load("../res/image/bullet.png")
IMG_BACK_BUTTON = pygame.transform.scale(IMG_BACK_BUTTON, (BACK_BUTTON_WIDTH, BACK_BUTTON_HEIGHT))

# gameOver # 검열
# IMG_GAMEOVER_BACKGROUND = pygame.image.load("../res/image/sangmin3.jpg")
# IMG_GAMEOVER_BACKGROUND = pygame.transform.scale(IMG_GAMEOVER_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))