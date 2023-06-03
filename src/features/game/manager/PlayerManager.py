from src.mysql.LifeCycleManager import *
from features.game.manager.StageManager import *
from src.entity.Bullet import *

class PlayerManager:

    def managePlayer(self):
        if Player.playerHp <= 0:
            LifeCycleManager.isPause = True
            LifeCycleManager.isPlaying = False
            LifeCycleManager.isSetting = False
            LifeCycleManager.isGameOver = True
            Player.initPlayer(Player)
            BulletManager.bulletList.clear()
            SangMinManager.sangMinList.clear()
            StageManager.stage = 1
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