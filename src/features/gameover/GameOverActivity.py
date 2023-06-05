import pygame

from util.lifeCycle import LifeCycleManager


class GameOverActivity:
    def init(self):
        from Container import container
        self.gameOverPainter = container["gameOverPainter"]
        self.gameOverPainter.init()
        self.__buttonViewList = self.gameOverPainter.getButtonViewList()
        self.__isDraw = False

    def onMouseClick(self):
        from Container import container
        toMainButtonView = self.__buttonViewList["homeButtonView"]
        replayButtonView = self.__buttonViewList["replayButtonView"]
        lifeCycleManager = container["lifeCycleManager"]
        player = container["player"]
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if toMainButtonView.isOnClick(mousePos):
                    lifeCycleManager.isGameOverActivity = False
                    lifeCycleManager.isMainActivity = True
                    player.init()
                if replayButtonView.isOnClick(mousePos):
                    lifeCycleManager.isGameOverActivity = False
                    lifeCycleManager.isGameActivity = True
                    lifeCycleManager.isPause = False
                    lifeCycleManager.isMainActivity = False
                    player.init()
            if event.type == pygame.QUIT:
                pygame.quit()

    def startGameOver(self):
        from Container import container, display
        gameOverPainter = container["gameOverPainter"]
        lifeCycleManager = container["lifeCycleManager"]
        if lifeCycleManager.isGameOverActivity:
            if not self.__isDraw:
                gameOverPainter.paint()
                display.update()
                self.__isDraw = True
        while lifeCycleManager.isGameOverActivity:
            self.onMouseClick()