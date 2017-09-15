class Level:
    def __init__(self, background, screen, charPos):
        self.x = 0
        self.y = 0
        self.background = background
        self.screen = screen
        self.size = background.get_rect().size


    def update(self, x, y):
        charSize = (20, 20)

        maxX = self.size[0] / 2 - charSize[0]
        maxY = self.size[1] / 2 - charSize[1]

        print('<', maxX, ',', maxY, '> - mosqito <', self.x, self.y,'> acc <', x, ',', y, '>')

        # if(abs(self.x + x) < maxX):
        #     self.x += x
        #     print(self.x)
        # if (abs(self.y + y) < maxY):
        #     self.y += y
        
        if(x > 0 and self.x <= 0):
            self.x += x

        if (x < 0 and self.x >= -maxX):
            self.x += x

        if (y > 0 and self.y <= 0):
            self.y += y

        if (y < 0 and self.y >= -maxY):
            self.y += y

    def draw(self):
        self.screen.blit(self.background, (self.x, self.y))