import pygame

import Container
from features.game.manager.PlayerManager import initAll


class PauseFragment:
    def init(self):
        self.__settingPainter = Container.container["pausePainter"]
        self.__settingPainter.init()
        self.__buttonViewList = self.__settingPainter.getButtonViewList()

    def onClickMouse(self):
        lifeCycleManager = Container.container["lifeCycleManager"]
        playerManager = Container.container["playerManager"]
        closeButton = self.__settingPainter.getButtonViewList()["closeButtonView"]
        homeButton = self.__settingPainter.getButtonViewList()["homeButtonView"]
        soundButton = self.__settingPainter.getButtonViewList()["soundButtonView"]
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if closeButton.isOnClick(mousePos):
                    lifeCycleManager.isPause = False
                    lifeCycleManager.isPauseFragment = False
                if homeButton.isOnClick(mousePos):
                    initAll()
                if soundButton.isOnClick(mousePos):
                    print("music on/off")

            if event.type == pygame.QUIT:
                pygame.quit()


    def startPause(self):
        lifeCycleManager = Container.container["lifeCycleManager"]
        self.init()
        while lifeCycleManager.isPauseFragment:
            self.onClickMouse()
            self.__settingPainter.paint()
            Container.display.update()
