from src.wiget.View import *
import pygame


class ImageView(View):
    def __init__(self):
        super().__init__()
        self.__scale = None
        self.__image = pygame.image.load("../res/image/player1.png")

    def setScale(self, scale):
        self.__scale = scale
        self.__image = pygame.transform.scale(self.__image, scale)

    def setImageByPath(self, image):
        self.__image = pygame.image.load(image)
        return self

    def setImageByObject(self, image):
        self.__image = image

    def getImage(self):
        return self.__image

    def getScale(self):
        return self.__scale

    def getWidth(self):
        return self.__scale[0]

    def getHeight(self):
        return self.__scale[1]

    def isOnClick(self, pos):
        xPos, yPos = pos
        return self.getXPos() <= xPos <= self.getXPos() + self.getWidth() and self.getYPos() <= yPos <= self.getYPos() + self.getHeight()