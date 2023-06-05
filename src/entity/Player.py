from src.util.constants import *


class Player:
    def __init__(self):
        self.xPos = None
        self.yPos = None
        self.playerHp = None
        self.playerXp = None
        self.playerMaxXp = None
        self.isSpecial = None
        self.isSpecialing = None
        self.specialCnt = None
        self.beforeSpecialTime = None

    def init(self):
        self.xPos = PLAYER_INIT_XPOS
        self.yPos = PLAYER_INIT_YPOS
        self.playerHp = PLAYER_INIT_HP
        self.playerXp = 0
        self.playerMaxXp = PLAYER_INIT_MAX_XP
        self.isSpecial = False
        self.isSpecialing = False
        self.specialCnt = PLAYER_SPECIAL_BULLET_SHOOT_CNT
        self.beforeSpecialTime = None

    def toString(self):
        return f"""
    pos - {self.xPos}, {self.yPos}
    hp - {self.playerHp} / {"PLAYER_INIT_HP"}
    xp - {self.playerXp} / {self.playerMaxXp}
    
        """