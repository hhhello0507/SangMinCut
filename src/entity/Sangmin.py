from src.entity.MoveEntity import *
from src.util.constants import *


class SangMin(MoveEntity):
    def __init__(self, xPos, yPos):
        super().__init__(xPos, yPos, 0, 0, True, BULLET_WIDTH, BULLET_HEIGHT)