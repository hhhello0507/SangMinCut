from src.manager.LifeManager import *
from src.manager.SangMinManager import *
from src.manager.StageManager import *
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
            LifeManager.isSetting = False
            LifeManager.isGameOver = True
            Player.initPlayer(Player)
            BulletManager.bulletList.clear()
            SangMinManager.sangMinList.clear()
            StageManager.stage = 1
