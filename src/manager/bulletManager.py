class BulletManager:
    bulletList = []
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.data = data
            cls._init = True
    def manageBullet(self):
        for (idx, bullet) in enumerate(self.bulletList):
            if bullet.isActive:
                bullet.move()
            else:
                self.bulletList.pop(idx)