from src.info.drawInfo import DrawInfo
from src.view.mainActivity import *
from src.manager.sangMinManager import *
from src.manager.bulletManager import *
from src.entity.player import *
from src.util.resource import *


def drawGame():
    DrawInfo.screen.blit(IMG_BACKGROUND, (0, 0))
    DrawInfo.screen.blit(IMG_PLAYER, (Player.xPos, Player.yPos))
    DrawInfo.screen.blit(IMG_SETTING, (DrawInfo.settingButton.xPos, DrawInfo.settingButton.yPos))
    for bullet in BulletManager.bulletList:
        DrawInfo.screen.blit(IMG_BULLET, (bullet.xPos, bullet.yPos))
    for sangMin in SangMinManager.sangMinList:
        DrawInfo.screen.blit(IMG_SANGMIN, (sangMin.xPos, sangMin.yPos))
    DrawInfo.display.update()