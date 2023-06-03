from features.game.manager.SangMinManager import *
import time
class StageManager:
    stage = 1
    beforeTime = -1
    nextStageTime = 10



    def manageStage(self):
        if StageManager.beforeTime == -1:
            StageManager.beforeTime = time.time()
        now = time.time()
        if StageManager.beforeTime + StageManager.nextStageTime < now:
            StageManager.nextStageTime += 2
            StageManager.stage += 1
            StageManager.beforeTime = now
            SangMinManager.sangMinCreateTime1 *= 0.8
            SangMinManager.sangMinCreateTime2 *= 0.8
            print("sangMinCreateTime1 - %.6f sangMinCreateTime2 - %.6f" % (SangMinManager.sangMinCreateTime1, SangMinManager.sangMinCreateTime2))

def stageInit():
    StageManager.stage = 1
    StageManager.beforeTime = -1
    StageManager.nextStageTime = 10