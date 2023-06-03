from features.game.manager.SangMinManager import *
import time
class StageManager:
    stage = 1
    beforeTime = -1
    nextStageTime = 10

    def manageStage(self):
        if self.beforeTime == -1:
            self.beforeTime = time.time()
        now = time.time()
        if self.beforeTime + self.nextStageTime < now:
            self.nextStageTime += 2
            self.stage += 1
            self.beforeTime = now
            SangMinManager.sangMinCreateTime1 *= 0.8
            SangMinManager.sangMinCreateTime2 *= 0.8
            print("sangMinCreateTime1 - %.6f sangMinCreateTime2 - %.6f" % (SangMinManager.sangMinCreateTime1, SangMinManager.sangMinCreateTime2))