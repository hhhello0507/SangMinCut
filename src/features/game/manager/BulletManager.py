class BulletManager:
    bulletList = []
    def manageBullet(self):
        for (idx, bullet) in enumerate(self.bulletList):
            if bullet.isActive:
                bullet.move()
            else:
                self.bulletList.pop(idx)