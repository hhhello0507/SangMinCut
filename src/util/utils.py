import random
import math

from src.util.constants import *

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 960
HOJOON_HEIGHT = 30


# 닮음 비 & 원 방정식 이용
def normalized(x, y):
    return x / ((x ** 2 + y ** 2) ** 0.5), y / ((x ** 2 + y ** 2) ** 0.5)

# 이차함수 이용
def getInclination(x, y, h, s):
    return (y - h) / ((x - s) ** 2)

# 갈 이차함수 계산
def setGalQuadraticGraph(gal):
    if gal.d:
        gal.s = gal.xPos + random.uniform(200, 300)
    else:
        gal.s = gal.xPos - random.uniform(200, 300)
    gal.h = random.uniform(100, 300)
    gal.a = getInclination(gal.xPos, gal.yPos, gal.h, gal.s)

def setHojoonThreeSin(hojoon):
    global SCREEN_HEIGHT, SCREEN_WIDTH, HOJOON_HEIGHT
    n = 0.1
    hojoon.a = random.uniform(-n, n)
    hojoon.b = random.uniform(-n, n)
    hojoon.c = random.uniform(-n, n)
    hojoon.h = random.uniform(SCREEN_HEIGHT / 5, SCREEN_HEIGHT - SCREEN_HEIGHT / 5 - HOJOON_HEIGHT)

def isObjectInMap(object):
    return -20 <= object.yPos <= SCREEN_HEIGHT and -20 <= object.xPos <= SCREEN_WIDTH

def adasd(degree):
    return normalized(1, math.tan(math.radians(degree)))

