import Container
from src.entity.Player import playerInit
from src.util.lifeCycle import *
import pygame


class MainActivity:
    def init(self):
        self.__mainPainter = Container.container["mainPainter"]
        self.__mainPainter.init()
        self.__buttonViewList = self.__mainPainter.getButtonViewList()

    def onMouseClick(self):
        startButton = self.__buttonViewList["playButtonView"]
        lifeCycleManager = Container.container["lifeCycleManager"]
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if startButton.isOnClick(mousePos):
                    lifeCycleManager.isMainActivity = False
                    lifeCycleManager.isGameActivity = True
                    lifeCycleManager.isPause = False
                    playerInit()
            if event.type == pygame.QUIT:
                pygame.quit()

    def startMain(self):
        lifeCycleManager = Container.container["lifeCycleManager"]
        if lifeCycleManager.isMainActivity:
            self.init()
        while lifeCycleManager.isMainActivity:
            self.onMouseClick()
            self.__mainPainter.paint()
            Container.display.update()
