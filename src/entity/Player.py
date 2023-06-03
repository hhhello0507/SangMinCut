from src.util.constants import *


class Player:
    xPos = None
    yPos = None
    playerHp = None
    playerXp = None
    playerMaxXp = None
    isSpecial = None
    isSpecialing = None
    specialCnt = None
    beforeSpecialTime = None

def playerInit():
    Player.xPos = PLAYER_INIT_XPOS
    Player.yPos = PLAYER_INIT_YPOS
    Player.playerHp = PLAYER_INIT_HP
    Player.playerXp = 0
    Player.playerMaxXp = PLAYER_INIT_MAX_XP
    Player.isSpecial = False
    Player.isSpecialing = False
    Player.specialCnt = PLAYER_SPECIAL_BULLET_SHOOT_CNT
    Player.beforeSpecialTime = None

def playerToString():
    return f"""
pos - {Player.xPos}, {Player.yPos}
hp - {Player.playerHp} / {"PLAYER_INIT_HP"}
xp - {Player.playerXp} / {Player.playerMaxXp}

    """