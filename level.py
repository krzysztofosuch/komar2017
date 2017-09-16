
class Level:
    def __init__(self, background, screen, charPos):
        self.x = charPos[0]
        self.y = charPos[1]
        self.background = background
        self.screen = screen
        self.size = background.get_rect().size


    def update(self, x, y):
        self.x = -x
        self.y = -y



    def draw(self):
        maxX = self.screen.get_size()[0] - self.size[0] / 2
        maxY = self.screen.get_size()[0] - self.size[1] / 2


        # if(self.x < 0):
        #     self.x = 1
        # elif(self.x > maxX):
        #     self.x = maxX

        print(self.x,', ',maxX)

        self.screen.blit(self.background, (self.x, self.y))