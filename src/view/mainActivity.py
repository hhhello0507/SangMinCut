import pygame

from src.info.lifeInfo import *
from src.manager.drawManager import *
from src.info.drawInfo import *

class MainAcitivty:
    # singleton
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.data = data
            cls._init = True
    def initPygame(self):
        pygame.init()
        DrawInfo.init(DrawInfo)


    # view
    def onMouseClick(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xMousePos, yMousePos) = pygame.mouse.get_pos()
                if DrawInfo.startButton.xPos <= xMousePos <= DrawInfo.startButton.xPos + DrawInfo.startButton.width and DrawInfo.startButton.yPos <= yMousePos <= DrawInfo.startButton.yPos + DrawInfo.startButton.height:
                    LifeInfo.isMain = False
                    LifeInfo.isPlaying = True
            if event.type == pygame.QUIT:
                exit(0)


    def startMain(self):
        # init
        self.initPygame(self)

        while LifeInfo.isMain:
            # event
            self.onMouseClick(self)

            # manager
            # pass

            # draw
            DrawManager.drawMain(DrawManager)
