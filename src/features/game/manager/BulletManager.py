import Container


class BulletManager:

    def __init__(self):
        self.bulletList = []

    def manageBullet(self):
        bulletManager = Container.container["bulletManager"]
        for (idx, bullet) in enumerate(self.bulletList):
            if bullet.isActive:
                bullet.move()
            else:
                bulletManager.bulletList.pop(idx)

    def init(self):
        self.bulletList.clear()
