from util.painter import *
from src.wiget.ButtonView import ButtonView
from src.util.constants import *

class PausePainter(Painter):
    def init(self):
        self._buttonViewList = {
            "soundButtonView":
                ButtonView() \
                    .setPos((746, 420)) \
                    .setImageByPath("../res/image/pause_music1.png") \
                    .setScale((100, 100)),
            "homeButtonView":
                ButtonView() \
                    .setPos((595, 420)) \
                    .setImageByPath("../res/image/pause_home.png") \
                    .setScale((100, 100)),
            "closeButtonView":
                ButtonView() \
                    .setPos((545, 554)) \
                    .setImageByPath("../res/image/pause_close.png") \
                    .setScale((350, 71))
        }

        self._imageViewList = {
            "settingBackgroundImageView":
                ImageView() \
                    .setPos((440, 300))
                    .setImageByPath("../res/image/pause.png")
                    .setScale((573, 377))
        }

    def getButtonViewList(self):
        return self._buttonViewList
