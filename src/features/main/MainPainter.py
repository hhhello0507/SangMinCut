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
                    .setPos((491, 679)) \
                    .setImageByPath("../res/image/btn_play.png") \
                    .setScale((457, 93)),
            "rankingButtonView":
                ButtonView() \
                    .setPos((491, 795)) \
                    .setImageByPath("../res/image/btn_ranking.png") \
                    .setScale((457, 93))
        }

    def getButtonViewList(self):
        return self._buttonViewList

    def paint(self):
        self.__paintBackground()
        super().paint()

    def __paintBackground(self):
        from Container import screen
        screen.blit(IMG_MAIN_BACKGROUND, (0, 0))
