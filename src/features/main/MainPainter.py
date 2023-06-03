from util.painter import Painter
from src.wiget.ButtonView import ButtonView
from src.util.constants import *
from src.util.resource import *


class MainPainter(Painter):
    def init(self):
        self._buttonViewList = {
            "startButton":
                ButtonView() \
                    .setPos((SCREEN_WIDTH - 400, SCREEN_HEIGHT - 100)) \
                    .setImageByPath("../res/image/player1.png") \
                    .setScale((500, 100)) \
                    .setText("LET'S JAVA SANGMIN") \
                    .setTextPos((SCREEN_WIDTH - 310, SCREEN_HEIGHT - 65))
        }

    def getButtonViewList(self):
        return self._buttonViewList

    def paint(self):
        self.__paintBackground()
        super().paint()

    def __paintBackground(self):
        screen = Container.screen
        screen.blit(IMG_BACKGROUND, (0, 0))
