import pygame

from src.util.constants import *
from src.util.utils import *


class MoveEntity:
    def __init__(self, xPos, yPos, xMove, yMove, isActive, width, height):
        self.xPos = xPos
        self.yPos = yPos
        self.xMove = xMove
        self.yMove = yMove
        self.isActive = isActive
        self.width = width
        self.height = height
        self.objectRect = pygame.Rect(xPos, yPos, width, height)

    def move(self):
        if -self.width <= self.xPos <= SCREEN_WIDTH + self.width and -self.height <= self.yPos <= SCREEN_HEIGHT + self.height:
            # print(self.xPos, self.yPos)
            self.xPos += self.xMove
            self.yPos += self.yMove
            self.objectRect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)
        else:
            self.isActive = False

    def calcMove(self, xPos, yPos, speed):
        (self.xMove, self.yMove) = Utils.normalized(Utils, xPos - self.xPos, yPos - self.yPos)
        self.xMove *= speed
        self.yMove *= speed
