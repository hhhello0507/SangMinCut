class LifeCycleManager:
    isMain = True
    isPlaying = False
    isPause = False
    isSetting = False
    isGameOver = False
    def printStatus(self):
        print(f"""
        
isMain:  {self.isMain}
isPlaying: {self.isPlaying}
isPause: {self.isPause}
isSetting: {self.isSetting}

""")