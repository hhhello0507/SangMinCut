from features.game.manager.BladeManager import BladeManager, bladeInit
from features.game.manager.GalManager import GalManager, galInit
from features.game.manager.HoJoonManager import HoJoonManager, hoJoonInit
from features.game.manager.HpPotionManager import HpPotionManager, hpPotionInit
from features.game.manager.StageManager import *
from features.game.manager.XpPotionManager import XpPotionManager, xpPotionInit
from src.entity.Bullet import *
from util.lifeCycle import lifeCycleInit


class PlayerManager:

    def managePlayer(self):
        if Player.playerHp <= 0:
            lifeCycleManager = Container.container["lifeCycleManager"]
            self.initAll()
            lifeCycleManager.isMain = False
            lifeCycleManager.isPlaying = False
            lifeCycleManager.isPause = True
            lifeCycleManager.isGameOver = True

        if Player.playerHp > PLAYER_INIT_HP:
            Player.playerHp = PLAYER_INIT_HP
        if Player.playerXp >= Player.playerMaxXp:
            Player.playerXp = Player.playerMaxXp
            Player.isSpecial = True
        if Player.isSpecialing:
            now = time.time()
            if Player.specialCnt > 0:
                if now - Player.beforeSpecialTime > 0.5:
                    Player.specialCnt -= 1
                    for idx in range(PLAYER_SPECIAL_BULLETS_CNT):
                        Player.beforeSpecialTime = now
                        bullet = Bullet(Player.xPos, Player.yPos, PLAYER_SPECIAL_BULLET_DEGREE[idx][0] * BULLET_SPEED,
                                        PLAYER_SPECIAL_BULLET_DEGREE[idx][1] * BULLET_SPEED)
                        BulletManager.bulletList.append(bullet)
            else:
                Player.specialCnt = PLAYER_SPECIAL_BULLET_SHOOT_CNT
                Player.isSpecialing = False
                Player.isSpecial = False

    def initAll(self):
        gameOverActivity = Container.container["gameOverActivity"]
        lifeCycleInit()
        playerInit()
        bulletInit()
        sangMinInit()
        stageInit()
        gameOverActivity.init()
        bladeInit()
        galInit()
        hoJoonInit()
        hpPotionInit()
        xpPotionInit()