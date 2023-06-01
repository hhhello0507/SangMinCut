from src.util.constants import *
from src.entity.Potion import *
class XpPotion(Potion):
    def __init__(self, xPos, yPos):
        self.xp = 10
        super().__init__(xPos, yPos, True, HP_POTION_WIDTH, HP_POTION_HEIGHT)