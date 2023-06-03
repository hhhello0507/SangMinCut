import Container
from src.entity.Player import *
from src.mysql.Painter import *
from src.wiget.ButtonView import *
from src.util.resource import *


class GamePainter(Painter):
    def init(self):
        self._buttonList = {
            "settingButton":
                ButtonView() \
                    .setPos((0, 0)) \
                    .setImageByPath("../res/image/player1.png") \
                    .setScale((200, 100)) \
                    .setText("설정") \
                    .setTextPos((100, 100)),
            "soundButton":
                ButtonView() \
                    .setPos((0, 0)) \
                    .setImageByPath("../res/image/player1.png") \
                    .setScale((200, 100)) \
                    .setText("소리") \
                    .setTextPos((100, 100)),
            "closeButton":
                ButtonView() \
                    .setPos((0, 0)) \
                    .setImageByPath("../res/image/player1.png") \
                    .setScale((200, 100)) \
                    .setText("닫기") \
                    .setTextPos((100, 100)),
            "backButton":
                ButtonView() \
                    .setPos((0, 0)) \
                    .setImageByPath("../res/image/player1.png") \
                    .setScale((200, 100)) \
                    .setText("뒤로") \
                    .setTextPos((100, 100))
        }

        self._textViewList = {
            "hpText":
                TextView() \
                    .setPos((Player.xPos, Player.yPos)),
            "xpText":
                TextView() \
                    .setPos((Player.xPos, Player.yPos + 30)),
            "stageText":
                TextView() \
                    .setPos((SCREEN_WIDTH / 2 - 100, 20))
        }

    def paint(self):
        self.__paintBackground()
        self.__paintPlayer()
        super().paint()
        self.__paintSangMin()
        self.__paintBullet()
        self.__paintHoJoon()
        self.__paintGal()
        self.__paintXpPotion()
        self.__paintHpPotion()
        Container.display.update()

    def __paintSangMin(self):
        for sangMin in Container.container["sangMinManager"].sangMinList:
            Container.screen.blit(IMG_SANGMIN, (sangMin.xPos, sangMin.yPos))

    def __paintBullet(self):
        for bullet in Container.container["bulletManager"].bulletList:
            Container.screen.blit(IMG_BULLET, (bullet.xPos, bullet.yPos))

    def __paintHoJoon(self):
        for hoJoon in Container.container["hoJoonManager"].hojoonList:
            Container.screen.blit(IMG_HOJOON, (hoJoon.xPos, hoJoon.yPos))

    def __paintGal(self):
        for gal in Container.container["galManager"].galList:
            Container.screen.blit(IMG_GAL, (gal.xPos, gal.yPos))

    def __paintXpPotion(self):
        for xpPotion in Container.container["xpPotionManager"].xpPotionList:
            Container.screen.blit(IMG_XP_POTION, (xpPotion.xPos, xpPotion.yPos))

    def __paintHpPotion(self):
        for hpPotion in Container.container["hpPotionManager"].hpPotionList:
            Container.screen.blit(IMG_HP_POTION, (hpPotion.xPos, hpPotion.yPos))

    def __paintPlayer(self):
        Container.screen.blit(IMG_PLAYER, (Player.xPos, Player.yPos))

    def __paintBackground(self):
        settingButton = self._buttonList["settingButton"]
        screen = Container.screen
        screen.blit(IMG_BACKGROUND, (0, 0))
        screen.blit(IMG_SETTING_BUTTON, (settingButton.getXPos(), settingButton.getYPos()))


    def getButtonViewList(self):
        return self._buttonList
