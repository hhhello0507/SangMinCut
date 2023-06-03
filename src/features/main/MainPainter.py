from src.mysql.Painter import Painter
from src.wiget.ButtonView import ButtonView
from src.util.constants import *

class MainPainter(Painter):
    def init(self):
        self._buttonList = {
            "startButton":
                ButtonView() \
                    .setPos((SCREEN_WIDTH - 400, SCREEN_HEIGHT - 100)) \
                    .setImageByPath("../res/image/player1.png") \
                    .setScale((500, 100)) \
                    .setText("LET'S JAVA SANGMIN") \
                    .setTextPos((SCREEN_WIDTH - 310, SCREEN_HEIGHT - 65))
        }

    def getButtonList(self):
        return self._buttonList
