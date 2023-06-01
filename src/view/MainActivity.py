from src.manager.LifeManager import *
from src.manager.DrawManager import *
from src.manager.DrawManager import *

class MainAcitivty:
    # singleton
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.data = data
            cls._init = True

    def initPygame(self):
        pygame.init()
        DrawManager.init(DrawManager)

    # view
    def onMouseClick(self):
        # print("onMouse")
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xMousePos, yMousePos) = pygame.mouse.get_pos()
                if DrawManager.startButton.xPos <= xMousePos <= DrawManager.startButton.xPos + DrawManager.startButton.width and DrawManager.startButton.yPos <= yMousePos <= DrawManager.startButton.yPos + DrawManager.startButton.height:
                    LifeManager.isMain = False
                    LifeManager.isPlaying = True
                    LifeManager.isPause = False

    def startMain(self):
        # init
        self.initPygame(self)

        while LifeManager.isMain:
            # event
            self.onMouseClick(self)

            # manager
            # pass

            # draw
            DrawManager.drawMain(DrawManager)
