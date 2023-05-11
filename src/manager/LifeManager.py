class LifeManager:
    isMain = True
    isPlaying = False
    isPause = False
    isSetting = False
    def printStatus(self):
        print(f"""
        
isMain:  {self.isMain}
isPlaying: {self.isPlaying}
isPause: {self.isPause}
isSetting: {self.isSetting}

""")