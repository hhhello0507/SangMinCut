from src.mysql.Painter import *
from src.wiget.ButtonView import ButtonView


class SettingPainter(Painter):
    def init(self):
        self._buttonViewList = {
            "soundButton":
                ButtonView() \
                    .setPos((0, 0)) \
                    .setImageByPath("../res/image/player1.png") \
                    .setScale((200, 100)) \
                    .setText("sound") \
                    .setTextPos((100, 100)),
            "closeButton":
                ButtonView() \
                    .setPos((0, 0)) \
                    .setImageByPath("../res/image/player1.png") \
                    .setScale((200, 100)) \
                    .setText("close") \
                    .setTextPos((100, 200)),
            "backButton":
                ButtonView() \
                    .setPos((0, 0)) \
                    .setImageByPath("../res/image/player1.png") \
                    .setScale((200, 100)) \
                    .setText("back") \
                    .setTextPos((100, 300))
        }
    def getButtonViewList(self):
        return self._buttonViewList
