from Container import container
import pygame

pygame.init()
pygame.display.set_caption("SangMinCut!!")

mainActivity = container["mainActivity"]
gameActivity = container["gameActivity"]
gameOverActivity = container["gameOverActivity"]

lifeCycleManager = container["lifeCycleManager"]

while True:
    mainActivity.startMain()
    gameActivity.startGame()
    gameOverActivity.startGameOver()
