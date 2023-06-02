from src.entity.MoveEntity import *
from src.util.constants import *
from src.util.resource import *


class Hojoon(MoveEntity):
    def __init__(self, xPos, yPos):
        self.a = None
        self.b = None
        self.c = None
        self.h = None
        super().__init__(xPos, yPos, 0, 0, True, GAL_WIDTH, GAL_HEIGHT)
