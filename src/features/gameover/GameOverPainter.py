from src.util.painter import *
from src.wiget.ButtonView import *
from src.util.constants import *
from src.util.resource import *


class GameOverPainter(Painter):
    def init(self):
        self._buttonViewList = {
            "toMainButtonView": ButtonView() \
                .setPos((100, 100)) \
                .setText("toMain")
                .setTextPos((100, 100))
                .setScale((200, 100))
                .setImageByPath("../res/image/player1.png"),
            "replayButtonView": ButtonView() \
                .setPos((430, 100)) \
                .setText("replay")
                .setTextPos((230, 100))
                .setScale((200, 100))
                .setImageByPath("../res/image/player1.png")
        }

    def paint(self):
        self.__paintBackground()
        super().paint()

    def __paintBackground(self):
        screen = Container.screen
        screen.blit(IMG_BACKGROUND, (0, 0))

    def getButtonViewList(self):
        return self._buttonViewList