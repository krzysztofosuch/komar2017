class Level:
    global DIRECT_DICT

    def __init__(self, background, screen):
        self.y = 0
        self.x = 0
        self.background = background
        self.screen = screen

    def update(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        self.screen.blit(self.background, (self.x, self.y))