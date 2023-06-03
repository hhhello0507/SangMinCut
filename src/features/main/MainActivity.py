import Container
from src.mysql.LifeCycleManager import *
import pygame


class MainActivity:
    def __init__(self):
        self.__mainPainter = None
        self.__buttonList = None

    def init(self):
        self.__mainPainter = Container.container["mainPainter"]
        self.__mainPainter.init()
        self.__buttonList = self.__mainPainter.getButtonList()

    def onMouseClick(self):
        startButton = self.__buttonList["startButton"]
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if startButton.isOnClick(mousePos):
                    LifeCycleManager.isMain = False
                    LifeCycleManager.isPlaying = True
                    LifeCycleManager.isPause = False

    def startMain(self):
        self.init()
        while LifeCycleManager.isMain:
            self.onMouseClick()
            self.__mainPainter.paint()
