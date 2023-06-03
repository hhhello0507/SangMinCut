from src.wiget.ImageView import *


class TextView(View):
    def __init__(self):
        super().__init__()
        self.__textView = None
        self.__text = None
        self.__color = (20, 20, 20)
        self.__textSize = 30

    def setText(self, text):
        self.__text = text
        self.__reloadText()
        return self

    def getText(self):
        return self.__text

    def setTextColor(self, color):
        self.__color = color
        self.__reloadText()
        return self

    def getTextView(self):
        return self.__textView

    def setTextSize(self, textSize):
        self.__textSize = textSize
        self.__reloadText()
        return self

    def getTextSize(self):
        return self.__textSize

    def __reloadText(self):
        font = pygame.font.Font("../res/font/arial.ttf", self.__textSize)
        self.__textView = font.render(self.__text, False, self.__color)
