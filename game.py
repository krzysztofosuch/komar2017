class Game:
    SCENE_MENU = 'Menu'
    SCENE_GAME = 'Game'

    def __init__(self, screen):
        self.scene = Game.SCENE_MENU
        self.screen = screen
        self.enabled = True
