from src.entity.Bullet import *

class PlayerManager:
    def managePlayer(self):
        from Container import container

        player = container["player"]
        if player.playerHp <= 0:
            lifeCycleManager = container["lifeCycleManager"]
            initAll()
            lifeCycleManager.isMainActivity = False
            lifeCycleManager.isGameActivity = False
            lifeCycleManager.isPause = True
            lifeCycleManager.isGameOverActivity = True

        if player.playerHp > PLAYER_INIT_HP:
            player.playerHp = PLAYER_INIT_HP
        if player.playerXp >= player.playerMaxXp:
            player.playerXp = player.playerMaxXp
            player.isSpecial = True
        if player.isSpecialing:
            now = time.time()
            if player.specialCnt > 0:
                if now - player.beforeSpecialTime > 0.5:
                    player.specialCnt -= 1
                    for idx in range(PLAYER_SPECIAL_BULLETS_CNT):
                        player.beforeSpecialTime = now
                        bullet = Bullet(player.xPos, player.yPos, PLAYER_SPECIAL_BULLET_DEGREE[idx][0] * BULLET_SPEED,
                                        PLAYER_SPECIAL_BULLET_DEGREE[idx][1] * BULLET_SPEED)
                        container["bulletManager"].bulletList.append(bullet)
            else:
                player.specialCnt = PLAYER_SPECIAL_BULLET_SHOOT_CNT
                player.isSpecialing = False
                player.isSpecial = False

def initAll():
    from Container import container
    container["gameOverActivity"].init()
    container["lifeCycleManager"].init()
    container["player"].init()
    container["bulletManager"].init()
    container["sangMinManager"].init()
    container["bladeManager"].init()
    container["stageManager"].init()
    container["galManager"].init()
    container["hoJoonManager"].init()
    container["hpPotionManager"].init()
    container["xpPotionManager"].init()
