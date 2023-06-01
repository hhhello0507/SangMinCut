import random
from src.util.constants import *

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
            print(gal.s)
        gal.h = random.uniform(100, 300)
        gal.a = self.getInclination(self, gal.xPos, gal.yPos, gal.h, gal.s)
