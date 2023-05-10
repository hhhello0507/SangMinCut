def drawScene():
    screen.blit(IMG_BACKGROUND, (0, 0))
    screen.blit(IMG_PLAYER, (xPos, yPos))
    screen.blit(IMG_SETTING, (settingButton.xPos, settingButton.yPos))
    for bullet in bulletList:
        screen.blit(IMG_BULLET, (bullet.xPos, bullet.yPos))
    for sangMin in sangMinList:
        screen.blit(IMG_SANGMIN, (sangMin.xPos, sangMin.yPos))
    display.update()