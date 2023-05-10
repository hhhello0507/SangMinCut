from src.util.constants import *


class MoveObject:
    def __init__(self, xPos, yPos, xMove, yMove, isActive, width, height):
        self.xPos = xPos
        self.yPos = yPos
        self.xMove = xMove
        self.yMove = yMove
        self.isActive = isActive
        self.width = width
        self.height = height

    def move(self):
        if -self.width <= self.xPos <= SCREEN_WIDTH + self.width and -self.height <= self.yPos <= SCREEN_HEIGHT + self.height:
            print(self.xPos, self.yPos)
            self.xPos += self.xMove
            self.yPos += self.yMove
        else:
            self.isActive = False
