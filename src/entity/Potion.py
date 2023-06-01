import pygame

class Potion:
    def __init__(self, xPos, yPos, isActive, width, height):
        self.xPos = xPos
        self.yPos = yPos
        self.isActive = isActive
        self.width = width
        self.height = height
        self.objectRect = pygame.Rect(xPos, yPos, width, height)