import Container


class LifeCycleManager:
    def __init__(self):
        self.isMainActivity = True
        self.isGameActivity = False
        self.isPause = False
        self.isPauseFragment = False
        self.isGameOverActivity = False

def lifeCycleInit():
    lifeCycleManager = Container.container["lifeCycleManager"]
    lifeCycleManager.isMainActivity = True
    lifeCycleManager.isGameActivity = False
    lifeCycleManager.isPause = True
    lifeCycleManager.isPauseFragment = False
    lifeCycleManager.isGameOverActivity = False