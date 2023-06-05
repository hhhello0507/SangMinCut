import Container
from features.game.manager.StageManager import StageManager
from src.entity.Player import *
from util.painter import *
from src.wiget.ButtonView import *
from src.util.resource import *
import time

class GamePainter(Painter):
    def init(self):
        from Container import container
        player= container["player"]
        self._buttonViewList = {
            "pauseButtonView":
                ButtonView() \
                    .setPos((1300, 48)) \
                    .setImageByPath("../res/image/btn_pause.png") \
                    .setScale((100, 100))
        }

        self._imageViewList = {
            "stageImageView":
                ImageView() \
                    .setPos((491, 60)) \
                    .setScale((457, 93)) \
                    .setImageByPath("../res/image/stage.png")
        }
        self._textViewList = {
            "hpTextView":
                TextView() \
                    .setPos((player.xPos, player.yPos))
                    .setTextColor((255, 255, 0)),
            "xpTextView":
                TextView() \
                    .setPos((20, SCREEN_HEIGHT - 40)) \
                    .setTextColor((255, 255, 0)),
            "stageTextView":
                TextView() \
                    .setPos((SCREEN_WIDTH / 2 - 100, 84)) \
                    .setTextColor((0, 0, 0)) \
                    .setTextSize(50)
        }

    def paint(self):
        self.__paintBackground()
        self.__paintPlayer()
        self.__paintSangMin()
        self.__paintBullet()
        self.__paintHoJoon()
        self.__paintGal()
        self.__paintXpPotion()
        self.__paintHpPotion()
        super().paint()

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
        player = Container.container['player']
        Container.screen.blit(IMG_PLAYER, (player.xPos, player.yPos))

    def __paintBackground(self):
        screen = Container.screen
        screen.blit(Container.container["stageManager"].background, (0, 0))

    def update(self):
        self.__updateHpBar()
        self.__updateXpBar()
        self.__updateStageBar()

    def __updateHpBar(self):
        player = Container.container['player']
        hpTextView = self._textViewList["hpTextView"]
        hpTextView.setPos((player.xPos + 20, player.yPos))
        hpTextView.setText(f"{player.playerHp} / {PLAYER_INIT_HP}")

    def __updateXpBar(self):
        player = Container.container['player']
        xpTextView = self._textViewList["xpTextView"]
        xpTextView.setText("*" * (int(player.playerXp * (PLAYER_XP_TEXT_WIDTH / player.playerMaxXp))) + "-" * (int((player.playerMaxXp - player.playerXp) *  (PLAYER_XP_TEXT_WIDTH / player.playerMaxXp))))

    def __updateStageBar(self):
        stageManager = Container.container["stageManager"]
        stageTextView = self._textViewList["stageTextView"]
        stageTextView.setText(f"STAGE {stageManager.stage}")

    def getButtonViewList(self):
        return self._buttonViewList
