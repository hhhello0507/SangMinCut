from src.manager.LifeManager import *
class GameOverActivitiy:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.data = data
            cls._init = True
    def startGameOver(self):
        while LifeManager.isGameOver:
            pass
