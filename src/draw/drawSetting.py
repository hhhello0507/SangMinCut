def drawSetting():
    screen.blit(IMG_SOUND_BUTTON, (soundButton.xPos, soundButton.yPos))
    screen.blit(IMG_CLOSE_BUTTON, (closeButton.xPos, closeButton.yPos))
    screen.blit(IMG_BACK_BUTTON, (backButton.xPos, backButton.yPos))
    display.update()