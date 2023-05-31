from src.entity.Player import *
from src.util.constants import *
from src.manager.SangMinManager import *

class StageManager:
    stage = 1
    def manageStage(self):
        if Player.playerXP >= Player.playerMaxXP:
            Player.playerXP = 0
            Player.playerMaxXP = int(Player.playerMaxXP * 1.2)
            SangMinManager.sangMinCreateTime1 *= 0.8
            SangMinManager.sangMinCreateTime2 *= 0.8
            self.stage += 1
            print("sangMinCreateTime1 - %.6f sangMinCreateTime2 - %.6f" %(SangMinManager.sangMinCreateTime1, SangMinManager.sangMinCreateTime2))