from src.features.gameover.GameOverPainter import GameOverPainter
from src.features.game.manager.HoJoonManager import HoJoonManager
from src.features.game.manager.HpPotionManager import HpPotionManager
from src.features.game.manager.GalManager import GalManager
from src.features.game.manager.XpPotionManager import XpPotionManager
from src.features.game.pause.PausePainter import *
from src.features.game.manager.BladeManager import *
from src.features.game.GamePainter import *
from src.features.main.MainPainter import *
from src.features.main.MainActivity import *
from src.features.game.GameActivity import *
from src.features.gameover.GameOverActivity import *

container = {
    # tools
    "lifeCycleManager": LifeCycleManager(),

    # game
    "mainActivity": MainActivity(),
    "mainPainter": MainPainter(),

    # game
    "gameActivity": GameActivity(),
    "gamePainter": GamePainter(),

    # game-manager
    "bulletManager": BulletManager(),
    "galManager": GalManager(),
    "hoJoonManager": HoJoonManager(),
    "playerManager": PlayerManager(),
    "stageManager": StageManager(),
    "sangMinManager": SangMinManager(),
    "hpPotionManager": HpPotionManager(),
    "xpPotionManager": XpPotionManager(),
    "bladeManager": BladeManager(),

    # game-etc
    "pausePainter": PausePainter(),
    "player": Player(),

    # gameOver
    "gameOverActivity": GameOverActivity(),
    "gameOverPainter": GameOverPainter()
}

display = pygame.display
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))