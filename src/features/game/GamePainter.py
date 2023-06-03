from src.mysql.Painter import *
from src.wiget.ButtonView import *


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


    def getButtonList(self):
        return self._buttonList
