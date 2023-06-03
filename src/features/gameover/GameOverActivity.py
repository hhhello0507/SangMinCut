import Container
import pygame

from src.entity.Player import playerInit
from src.util.utils import printStatus


class GameOverActivity:
    def init(self):
        container = Container.container
        self.gameOverPainter = container["gameOverPainter"]
        self.gameOverPainter.init()
        self.__buttonViewList = self.gameOverPainter.getButtonViewList()

    def onMouseClick(self):
        toMainButtonView = self.__buttonViewList["toMainButtonView"]
        replayButtonView = self.__buttonViewList["replayButtonView"]
        lifeCycleManager = Container.container["lifeCycleManager"]
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if toMainButtonView.isOnClick(mousePos):
                    lifeCycleManager.isGameOver = False
                    lifeCycleManager.isMain = True
                    playerInit()
                    printStatus()
                if replayButtonView.isOnClick(mousePos):
                    lifeCycleManager.isGameOver = False
                    lifeCycleManager.isPlaying = True
                    lifeCycleManager.isPause = False
                    lifeCycleManager.isMain = False
                    playerInit()
            if event.type == pygame.QUIT:
                pygame.quit()

    def startGameOver(self):
        lifeCycleManager = Container.container["lifeCycleManager"]
        gameOverPainter = Container.container["gameOverPainter"]
        while lifeCycleManager.isGameOver:
            self.onMouseClick()
            gameOverPainter.paint()
            Container.display.update()