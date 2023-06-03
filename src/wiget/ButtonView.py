from src.wiget.ImageView import *
from src.wiget.TextView import *


class ButtonView(ImageView):
    def __init__(self):
        super().__init__()
        self.__textView = TextView()

    def setScale(self, scale):
        super().setScale(scale)
        return self

    def setPos(self, pos):
        super().setPos(pos)
        return self

    def setText(self, text):
        self.__textView.setText(text)
        return self

    def setTextPos(self, pos):
        self.__textView.setPos(pos)
        return self

    def setImageByPath(self, image):
        super().setImageByPath(image)
        return self

    def getTextView(self):
        return self.__textView

    def getImage(self):
        return super().getImage()