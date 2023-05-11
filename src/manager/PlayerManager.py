from src.manager.LifeManager import *
from src.manager.SangMinManager import *
class PlayerManager:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.data = data
            cls._init = True

    def managePlayer(self):
        if Player.playerHP == 0:
            LifeManager.isPause = True
            LifeManager.isPlaying = False
            LifeManager.isMain = True
            Player.xPos = PLAYER_INIT_XPOS
            Player.yPos = PLAYER_INIT_YPOS
            Player.playerHP = PLAYER_INIT_HP
            BulletManager.bulletList.clear()
            SangMinManager.sangMinList.clear()
