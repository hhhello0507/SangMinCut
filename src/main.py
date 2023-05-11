from src.view.MainActivity import *
from src.view.GameActivity import *
from src.view.GameOverActivity import *

while True:
    # print lifecycle status
    LifeManager.printStatus(LifeManager)

    # start activity
    MainAcitivty.startMain(MainAcitivty)
    GameActivity.startGame(GameActivity)
    GameOverActivitiy.startGameOver(GameOverActivitiy)