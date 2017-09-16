
class Level:
    def __init__(self, background, screen, mosquito):
        self.x = mosquito.x
        self.y = mosquito.y
        self.background = background
        self.screen = screen
        self.size = background.get_rect().size
        self.mosquito = mosquito
        self.mosquitoSize = self.mosquito.image.get_size()

    def update(self, x, y):
        self.x = x-(self.mosquitoSize[0]/2)
        self.y = y-(self.mosquitoSize[1]/2)
        


    def draw(self):
        maxX = self.screen.get_size()[0]
        maxY = self.screen.get_size()[1]
        centerX = self.screen.get_size()[0]/2
        centerY = self.screen.get_size()[1]/2
        maxMosquitoX = self.background.get_size()[0]
        maxMosquitoY = self.background.get_size()[1]
        if (self.x < centerX):
            mosquitoX = self.x
            bX = 0
        elif self.x < maxMosquitoX-centerX:
            mosquitoX = centerX
            bX = -self.x+centerX
        else:
            mosquitoX = centerX+(centerX-(maxMosquitoX-self.x))
            bX = -maxMosquitoX+maxX

        if (self.y < centerY):
            mosquitoY = self.y
            bY = 0
        elif self.y < maxMosquitoY-centerY:
            mosquitoY = centerY
            bY = -self.y+centerY
        else:
            mosquitoY = centerY+(centerY-(maxMosquitoY-self.y))
            bY = -maxMosquitoY+maxY

        self.screen.blit(self.background, (bX, bY))
        self.screen.blit(self.mosquito.current_image(), (mosquitoX, mosquitoY))
