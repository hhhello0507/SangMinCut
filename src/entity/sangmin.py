from src.entity.moveObject import *
from src.util.constants import *

class SangMin(MoveObject):
    def __init__(self, xPos, yPos):
        super().__init__(xPos, yPos, 0, 0, True, BULLET_WIDTH, BULLET_HEIGHT)