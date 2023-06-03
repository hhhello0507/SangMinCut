import Container
from src.entity.Player import *
from util.painter import *
from src.wiget.ButtonView import *
from src.util.resource import *
import time

class GamePainter(Painter):
    def init(self):
        self._buttonList = {
            "settingButtonView":
                ButtonView() \
                    .setPos((0, 0)) \
                    .setImageByPath("../res/image/player1.png") \
                    .setScale((200, 100)) \
                    .setText("설정") \
                    .setTextPos((100, 100))
        }

        self._textViewList = {
            "hpTextView":
                TextView() \
                    .setPos((Player.xPos, Player.yPos))
                    .setTextColor((255, 255, 0)),
            "xpTextView":
                TextView() \
                    .setPos((20, SCREEN_HEIGHT - 40)) \
                    .setTextColor((255, 255, 0)),
            "stageTextView":
                TextView() \
                    .setPos((SCREEN_WIDTH / 2 - 230, 20)) \
                    .setTextColor((255, 255, 0))
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
        settingButton = self._buttonList["settingButtonView"]
        screen = Container.screen
        screen.blit(IMG_BACKGROUND, (0, 0))
        screen.blit(settingButton.getImage(), (settingButton.getXPos(), settingButton.getYPos()))

    def update(self):
        self.__updateHpBar()
        self.__updateXpBar()
        self.__updateStageBar()

    def __updateHpBar(self):
        hpTextView = self._textViewList["hpTextView"]
        hpTextView.setPos((Player.xPos + 20, Player.yPos))
        hpTextView.setText(f"{Player.playerHp}/{PLAYER_INIT_HP}")

    def __updateXpBar(self):
        xpTextView = self._textViewList["xpTextView"]
        xpTextView.setText("*" * (int(Player.playerXp * (PLAYER_XP_TEXT_WIDTH / Player.playerMaxXp))) + "-" * (int((Player.playerMaxXp - Player.playerXp) *  (PLAYER_XP_TEXT_WIDTH / Player.playerMaxXp))))

    def __updateStageBar(self):
        stageManager = Container.container["stageManager"]
        stageTextView = self._textViewList["stageTextView"]
        stageTextView.setText(f"{stageManager.stage} STAGE :: NEXT STAGE: {math.ceil(stageManager.beforeTime + stageManager.nextStageTime - time.time())}")

    def getButtonViewList(self):
        return self._buttonList
