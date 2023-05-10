from src.model.moveObject import *


class Bullet(MoveObject):
    def __init__(self, xPos, yPos, xMove, yMove):
        super().__init__(xPos, yPos, xMove, yMove, True, BULLET_WIDTH, BULLET_HEIGHT)