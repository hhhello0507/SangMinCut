from util.painter import Painter
from src.wiget.ButtonView import ButtonView
from src.util.constants import *
from src.util.resource import *
from src.wiget.TextView import *


class MainPainter(Painter):
    def init(self):
        self._buttonViewList = {
            "playButtonView":
                ButtonView() \
                    .setPos((440, SCREEN_HEIGHT - 280)) \
                    .setImageByPath("../res/image/btn_play.png") \
                    .setScale((450, 100)),
            "rankingButtonView":
                ButtonView() \
                    .setPos((440, SCREEN_HEIGHT - 150)) \
                    .setImageByPath("../res/image/btn_ranking.png") \
                    .setScale((450, 100))
        }

    def getButtonViewList(self):
        return self._buttonViewList

    def paint(self):
        self.__paintBackground()
        super().paint()

    def __paintBackground(self):
        screen = Container.screen
        screen.blit(IMG_MAIN_BACKGROUND, (0, 0))
