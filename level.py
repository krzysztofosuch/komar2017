
class Level:
    def __init__(self, background, screen, mosquito):
        self.x = mosquito.x
        self.y = mosquito.y
        self.background = background
        self.screen = screen
        self.size = background.get_rect().size
        self.mosquito = mosquito


    def update(self, x, y):
        self.x = -x
        self.y = -y



    def draw(self):
        maxX = -self.screen.get_size()[0]
        maxY = -self.screen.get_size()[1]
        centerX = self.screen.get_size()[0]/2
        centerY = self.screen.get_size()[1]/2

        # print(self.size[0] - maxX)

        if(self.x > 0):
            bX = 0
        elif(self.x < maxX):
            bX = maxX
        else:
            bX = self.x

        if (self.x > 0):
            mosquitoX = centerX - self.x
        elif(self.x < maxX):
            mosquitoX = -centerX - self.x
        else:
            mosquitoX = centerX

        if (self.y > 0):
            bY = 0
            mosquitoY = -self.y
        elif (self.y < maxY):
            bY = maxY
            mosquitoY = -self.y
        else:
            bY = self.y
            mosquitoY = centerY

        if (self.y > 0):
            mosquitoY = centerY - self.y
        elif(self.y < maxY):
            mosquitoY = -centerY - self.y
        else:
            mosquitoY = centerY


        print(mosquitoX)
        print(self.x,', ',maxX)

        self.screen.blit(self.background, (bX, bY))
        self.screen.blit(self.mosquito.image, (mosquitoX, mosquitoY))