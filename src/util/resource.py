import pygame
from src.util.constants import *

IMG_MAIN_BACKGROUND = pygame.image.load("../res/image/background1.png")
IMG_MAIN_BACKGROUND = pygame.transform.scale(IMG_MAIN_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

IMG_GAME_BACKGROUND1 = pygame.image.load("../res/image/game_background1.png")
IMG_GAME_BACKGROUND1 = pygame.transform.scale(IMG_GAME_BACKGROUND1, (SCREEN_WIDTH, SCREEN_HEIGHT))

IMG_GAME_BACKGROUND2 = pygame.image.load("../res/image/game_background2.png")
IMG_GAME_BACKGROUND2 = pygame.transform.scale(IMG_GAME_BACKGROUND2, (SCREEN_WIDTH, SCREEN_HEIGHT))

IMG_GAME_BACKGROUND3 = pygame.image.load("../res/image/game_background3.png")
IMG_GAME_BACKGROUND3 = pygame.transform.scale(IMG_GAME_BACKGROUND3, (SCREEN_WIDTH, SCREEN_HEIGHT))

IMG_GAME_BACKGROUND4 = pygame.image.load("../res/image/game_background4.png")
IMG_GAME_BACKGROUND4 = pygame.transform.scale(IMG_GAME_BACKGROUND4, (SCREEN_WIDTH, SCREEN_HEIGHT))

IMG_GAME_BACKGROUND5 = pygame.image.load("../res/image/game_background5.png")
IMG_GAME_BACKGROUND5 = pygame.transform.scale(IMG_GAME_BACKGROUND5, (SCREEN_WIDTH, SCREEN_HEIGHT))

IMG_GAMEOVER_BACKGROUND = pygame.image.load("../res/image/gameover_background.png")
IMG_GAMEOVER_BACKGROUND = pygame.transform.scale(IMG_GAMEOVER_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

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

IMG_XP_POTION = pygame.image.load("../res/image/xp_potion.png")
IMG_XP_POTION = pygame.transform.scale(IMG_XP_POTION, (XP_POTION_WIDTH, XP_POTION_HEIGHT))

# gameOver # 검열
# IMG_GAMEOVER_BACKGROUND = pygame.image.load("../res/image/sangmin3.jpg")
# IMG_GAMEOVER_BACKGROUND = pygame.transform.scale(IMG_GAMEOVER_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))