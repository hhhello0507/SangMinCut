class View:
    def __init__(self):
        self._xPos = None
        self._yPos = None

    def setPos(self, pos):
        xPos, yPos = pos
        self._xPos = xPos
        self._yPos = yPos
        return self

    def getPos(self):
        return (self._xPos, self._yPos)

    def getXPos(self):
        return self._xPos

    def getYPos(self):
        return self._yPos