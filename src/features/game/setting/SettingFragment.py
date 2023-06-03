from src.mysql.LifeCycleManager import *
from src.mysql.DrawManager import *
import pygame

def settingFragment():
    while LifeCycleManager.isSetting:
        # TODO: onClickSoundButton()
        # TODO: onClickBackButton()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xMousePos, yMousePos) = pygame.mouse.get_pos()
                if DrawManager.soundButton.xPos <= xMousePos <= DrawManager.soundButton.xPos + DrawManager.soundButton.width and DrawManager.soundButton.yPos <= yMousePos <= DrawManager.soundButton.yPos + DrawManager.soundButton.height:
                    LifeCycleManager.isSetting = False
                    LifeCycleManager.isPause = False
            if event.type == pygame.QUIT:
                pygame.quit()
        DrawManager.drawSettingMap(DrawManager)