from src.info.lifeInfo import *
from src.info.drawInfo import *
from src.draw.drawSetting import *
import pygame

def settingFragment():
    while LifeInfo.isSetting:
        # TODO: onClickSoundButton()
        # TODO: onClickBackButton()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xMousePos, yMousePos) = pygame.mouse.get_pos()
                if DrawInfo.soundButton.xPos <= xMousePos <= DrawInfo.soundButton.xPos + DrawInfo.soundButton.width and DrawInfo.soundButton.yPos <= yMousePos <= DrawInfo.soundButton.yPos + DrawInfo.soundButton.height:
                    LifeInfo.isSetting = False
                    LifeInfo.isPause = False
            if event.type == pygame.QUIT:
                pygame.quit()
        drawSetting()