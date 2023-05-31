from src.util.constants import *


class Player:
    xPos = PLAYER_INIT_XPOS
    yPos = PLAYER_INIT_YPOS
    playerHP = PLAYER_INIT_HP
    playerXP = 0
    playerMaxXP = PLAYER_INIT_MAX_XP

    def initPlayer(self):
        self.xPos = PLAYER_INIT_XPOS
        self.yPos = PLAYER_INIT_YPOS
        self.playerHP = PLAYER_INIT_HP
        self.playerXP = 0
        self.playerMaxXP = PLAYER_INIT_MAX_XP

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.data = data
            cls._init = True
