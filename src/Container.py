from src.features.game.setting.SettingPainter import *
from src.features.game.manager.BladeManager import *
from src.features.game.GamePainter import *
from src.features.main.MainPainter import *
from src.features.main.MainActivity import *
from src.features.game.GameActivity import *
from src.features.gameover.GameOverActivity import *

container = {
    "lifeCycleManager": LifeCycleManager(),
    "utils": Utils(),

    "mainActivity": MainActivity(),
    "mainPainter": MainPainter(),

    "gameActivity": GameActivity(),
    "gamePainter": GamePainter(),
    "bulletManager": BulletManager(),
    "galManager": GalManager(),
    "hoJoonManager": HoJoonManager(),
    "playerManager": PlayerManager(),
    "stageManager": StageManager(),
    "sangMinManager": SangMinManager(),
    "hpPotionManager": HpPotionManager(),
    "xpPotionManager": XpPotionManager(),
    "bladeManager": BladeManager(),
    "settingPainter": SettingPainter(),

    "player": Player(),

    "gameOverActivity": GameOverActivity()


}

display = pygame.display
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))