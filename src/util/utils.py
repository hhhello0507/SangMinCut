import random
from src.util.constants import *
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 960
HOJOON_HEIGHT = 30

class Utils:
    # 싱글턴
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.data = data
            cls._init = True

    # 닮음 비 & 원 방정식 이용
    def normalized(self, x, y):
        return x / ((x ** 2 + y ** 2) ** 0.5), y / ((x ** 2 + y ** 2) ** 0.5)

    # 이차함수 이용
    def getInclination(self, x, y, h, s):
        return (y - h) / ((x - s) ** 2)

    # 갈 이차함수 계산
    def setGalQuadraticGraph(self, gal):
        if gal.d:
            gal.s = gal.xPos + random.uniform(200, 300)
        else:
            gal.s = gal.xPos - random.uniform(200, 300)
        gal.h = random.uniform(100, 300)
        gal.a = self.getInclination(self, gal.xPos, gal.yPos, gal.h, gal.s)

    def setHojoonThreeSin(self, hojoon):
        global SCREEN_HEIGHT, SCREEN_WIDTH, HOJOON_HEIGHT
        n = 0.1
        hojoon.a = random.uniform(-n, n)
        hojoon.b = random.uniform(-n, n)
        hojoon.c = random.uniform(-n, n)
        hojoon.h = random.uniform(SCREEN_HEIGHT / 5, SCREEN_HEIGHT - SCREEN_HEIGHT / 5 - HOJOON_HEIGHT)

    def isObjectInMap(self, object):
        return -20 <= object.yPos <= SCREEN_HEIGHT and -20 <= object.xPos <= SCREEN_WIDTH