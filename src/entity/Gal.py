from src.entity.MoveEntity import *
from src.util.constants import *


class Gal(MoveEntity):
    isJump = False
    def __init__(self, xPos, yPos):
        self.a = None # 기울기
        self.h = None # 높이
        self.s = None # 이차함수 꼭짓점 xPos
        self.d = None # 좌/우
        super().__init__(xPos, yPos, 0, 0, True, GAL_WIDTH, GAL_HEIGHT)
