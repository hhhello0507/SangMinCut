import pygame
from src.util.constants import *
from src.wiget.button import *

class DrawInfo:
    startButton = Button(SCREEN_WIDTH - BUTTON_WIDTH, SCREEN_HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
    settingButton = Button(0, 0, SETTING_WIDTH, SETTING_HEIGHT)
    soundButton = Button(0, 0, SOUND_BUTTON_WIDTH, SOUND_BUTTON_HEIGHT)
    closeButton = Button(100, 0, CLOSE_BUTTON_WIDTH, CLOSE_BUTTON_HEIGHT)
    backButton = Button(200, 0, BACK_BUTTON_WIDTH, BACK_BUTTON_HEIGHT)
    
    display = None

    screen = None

    font = None
    mainStartText = None

    def init(self):
        self.display = pygame.display
        self.display.set_caption("SangMinCut!!")

        self.screen = self.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.font = pygame.font.Font("../res/font/arial.ttf", 30)
        self.mainStartText = self.font.render("start", False, (20, 20, 20))
    def __init__(self):
        pass