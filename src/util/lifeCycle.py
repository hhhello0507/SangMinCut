class LifeCycleManager:
    def __init__(self):
        self.isMainActivity = True
        self.isGameActivity = False
        self.isPause = False
        self.isPauseFragment = False
        self.isGameOverActivity = False

    def init(self):
        self.isMainActivity = True
        self.isGameActivity = False
        self.isPause = True
        self.isPauseFragment = False
        self.isGameOverActivity = False