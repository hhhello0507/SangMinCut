class LifeCycleManager:
    isMain = True
    isPlaying = False
    isPause = False
    isSetting = False
    isGameOver = False

def lifeCycleInit():
    LifeCycleManager.isMain = True
    LifeCycleManager.isPlaying = False
    LifeCycleManager.isPause = False
    LifeCycleManager.isSetting = False
    LifeCycleManager.isGameOver = False