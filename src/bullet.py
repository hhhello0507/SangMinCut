from src.util.constants import *


class Bullet:
    def __init__(self, xPos, yPos, xMove, yMove):
        self.xPos = xPos
        self.yPos = yPos
        self.xMove = xMove
        self.yMove = yMove
        self.isActive = True

    def move(self):
        if -BULLET_WIDTH <= self.xPos <= SCREEN_WIDTH + BULLET_WIDTH and -BULLET_HEIGHT <= self.yPos <= SCREEN_HEIGHT + BULLET_HEIGHT:
            print(self.xPos, self.yPos)
            self.xPos += self.xMove
            self.yPos += self.yMove
        else:
            self.isActive = False
