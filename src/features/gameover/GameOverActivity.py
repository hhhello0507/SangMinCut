from src.mysql.LifeCycleManager import *
from src.mysql.DrawManager import *


class GameOverActivity:
    def onClick(self):
        pass

    def startGameOver(self):
        DrawManager.drawGameOver(DrawManager)
        while LifeCycleManager.isGameOver:
            pass