from moveObject import *


class Bullet(MoveObject):
    def __init__(self, xPos, yPos, xMove, yMove):
        super().__init__(xPos, yPos, xMove, yMove, True, BULLET_WIDTH, BULLET_HEIGHT)
    #
    # def move(self):
    #     if -self.width <= self.xPos <= SCREEN_WIDTH + self.width and -self.height <= self.yPos <= SCREEN_HEIGHT + self.height:
    #         # print(self.xPos, self.yPos)
    #         self.xPos += self.xMove
    #         self.yPos += self.yMove
    #     else:
    #         self.isActive = False
