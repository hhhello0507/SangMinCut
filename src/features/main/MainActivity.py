import Container
from src.entity.Player import playerInit
from src.util.lifeCycle import *
import pygame


class MainActivity:
    def init(self):
        self.__mainPainter = Container.container["mainPainter"]
        self.__mainPainter.init()
        self.__buttonViewList = self.__mainPainter.getButtonViewList()
        self.__isDraw = False

    def onMouseClick(self):
        startButton = self.__buttonViewList["playButtonView"]
        lifeCycleManager = Container.container["lifeCycleManager"]
        gameActivity = Container.container["gameActivity"]
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if startButton.isOnClick(mousePos):
                    lifeCycleManager.isMainActivity = False
                    lifeCycleManager.isGameActivity = True
                    lifeCycleManager.isPause = False
                    playerInit()
                    gameActivity.init()
            if event.type == pygame.QUIT:
                pygame.quit()

    def startMain(self):
        lifeCycleManager = Container.container["lifeCycleManager"]
        if lifeCycleManager.isMainActivity:
            self.init()
            if not self.__isDraw:
                self.__mainPainter.paint()
                Container.display.update()
                self.__isDraw = True
        while lifeCycleManager.isMainActivity:
            self.onMouseClick()
