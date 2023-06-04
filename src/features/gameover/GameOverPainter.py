from src.util.painter import *
from src.wiget.ButtonView import *
from src.util.constants import *
from src.util.resource import *


class GameOverPainter(Painter):
    def init(self):
        self._buttonViewList = {
            "replayButtonView": ButtonView() \
                .setPos((491, 679)) \
                .setScale((457, 93))
            .setImageByPath("../res/image/gameover_replay.png"),
            "homeButtonView": ButtonView() \
                .setPos((491, 795)) \
                .setScale((457, 93))
                .setImageByPath("../res/image/gameover_home.png")
        }

    def paint(self):
        self.__paintBackground()
        super().paint()

    def __paintBackground(self):
        screen = Container.screen
        screen.blit(IMG_GAMEOVER_BACKGROUND, (0, 0))

    def getButtonViewList(self):
        return self._buttonViewList