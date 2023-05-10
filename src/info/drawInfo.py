import pygame
from src.util.constants import *
from src.wiget.button import *

font = None
mainStartText = None

display = pygame.display
display.set_caption("SangMinCut!!")

screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

startButton = Button(SCREEN_WIDTH - BUTTON_WIDTH, SCREEN_HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
settingButton = Button(0, 0, SETTING_WIDTH, SETTING_HEIGHT)
soundButton = Button(0, 0, SOUND_BUTTON_WIDTH, SOUND_BUTTON_HEIGHT)
closeButton = Button(100, 0, CLOSE_BUTTON_WIDTH, CLOSE_BUTTON_HEIGHT)
backButton = Button(200, 0, BACK_BUTTON_WIDTH, BACK_BUTTON_HEIGHT)