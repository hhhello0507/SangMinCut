from src.util.constants import *


class Player:
    xPos = PLAYER_INIT_XPOS
    yPos = PLAYER_INIT_YPOS
    playerHp = PLAYER_INIT_HP
    playerXp = 0
    playerMaxXp = PLAYER_INIT_MAX_XP
    isSpecial = False
    isSpecialing = False
    specialCnt = PLAYER_SPECIAL_BULLET_SHOOT_CNT
    beforeSpecialTime = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.data = data
            cls._init = True

    def initPlayer(self):
        self.xPos = PLAYER_INIT_XPOS
        self.yPos = PLAYER_INIT_YPOS
        self.playerHp = PLAYER_INIT_HP
        self.playerXp = 0
        self.playerMaxXp = PLAYER_INIT_MAX_XP



