import Container
import pygame

from src.entity.Player import playerInit
from src.util.utils import printStatus
from util.lifeCycle import LifeCycleManager


class GameOverActivity:
    def init(self):
        container = Container.container
        self.gameOverPainter = container["gameOverPainter"]
        self.gameOverPainter.init()
        self.__buttonViewList = self.gameOverPainter.getButtonViewList()
        self.__isDraw = False

    def onMouseClick(self):
        toMainButtonView = self.__buttonViewList["homeButtonView"]
        replayButtonView = self.__buttonViewList["replayButtonView"]
        lifeCycleManager = Container.container["lifeCycleManager"]
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if toMainButtonView.isOnClick(mousePos):
                    lifeCycleManager.isGameOverActivity = False
                    lifeCycleManager.isMainActivity = True
                    playerInit()
                    printStatus()
                if replayButtonView.isOnClick(mousePos):
                    lifeCycleManager.isGameOverActivity = False
                    lifeCycleManager.isGameActivity = True
                    lifeCycleManager.isPause = False
                    lifeCycleManager.isMainActivity = False
                    playerInit()
            if event.type == pygame.QUIT:
                pygame.quit()

    def startGameOver(self):
        gameOverPainter = Container.container["gameOverPainter"]
        lifeCycleManager = Container.container["lifeCycleManager"]
        if lifeCycleManager.isGameOverActivity:
            if not self.__isDraw:
                gameOverPainter.paint()
                Container.display.update()
                self.__isDraw = True
        while lifeCycleManager.isGameOverActivity:
            self.onMouseClick()