class BulletManager:
    bulletList = []

    def manageBullet(self):
        for (idx, bullet) in enumerate(self.bulletList):
            if bullet.isActive:
                bullet.move()
            else:
                BulletManager.bulletList.pop(idx)

def bulletInit():
    BulletManager.bulletList.clear()

