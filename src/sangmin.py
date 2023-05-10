from moveObject import *


class SangMin(MoveObject):
    def __init__(self, xPos, yPos, xMove, yMove):
        super().__init__(xPos, yPos, xMove, yMove, True, BULLET_WIDTH, BULLET_HEIGHT)

    def move(self):
        if -BULLET_WIDTH <= self.xPos <= SCREEN_WIDTH + BULLET_WIDTH and -BULLET_HEIGHT <= self.yPos <= SCREEN_HEIGHT + BULLET_HEIGHT:
            print(self.xPos, self.yPos)
            self.xPos += self.xMove
            self.yPos += self.yMove
        else:
            self.isActive = False
