import pygame

import Container


class SettingFragment:
    def init(self):
        self.__settingPainter = Container.container["settingPainter"]
        self.__settingPainter.init()
        self.__buttonViewList = self.__settingPainter.getButtonViewList()

    def onClickMouse(self):
        lifeCycleManager = Container.container["lifeCycleManager"]
        settingPainter = Container.container["settingPainter"]
        soundButton = settingPainter.getButtonViewList()["soundButton"]
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xMousePos, yMousePos) = pygame.mouse.get_pos()
                if soundButton.getXPos() <= xMousePos <= soundButton.getXPos() + soundButton.getWidth() and soundButton.getYPos() <= yMousePos <= soundButton.getYPos() + soundButton.getHeight():
                    lifeCycleManager.isSetting = False
                    lifeCycleManager.isPause = False
            if event.type == pygame.QUIT:
                pygame.quit()


    def startSetting(self):
        lifeCycleManager = Container.container["lifeCycleManager"]
        self.init()
        while lifeCycleManager.isSetting:
            self.onClickMouse()
            self.__settingPainter.paint()
            Container.display.update()
