import Container
from src.mysql.LifeCycleManager import *
import pygame


class MainActivity:
    def init(self):
        self.__mainPainter = Container.container["mainPainter"]
        self.__mainPainter.init()
        self.__buttonViewList = self.__mainPainter.getButtonViewList()

    def onMouseClick(self):
        startButton = self.__buttonViewList["startButton"]
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
            Container.display.update()
