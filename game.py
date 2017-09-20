class Game:
    SCENE_MENU = 'Menu'
    SCENE_GAME = 'Game'
    SCENE_RESTART = 'Restart'
    SCENE_CREDITS = 'Credits'
    SCENE_GAME_OVER = 'Game Over'
    SCENE_RUN = "Run"

    def __init__(self, screen):
        self.scene = Game.SCENE_MENU
        self.screen = screen
        self.enabled = True
        self.main_menu = None
        self.restart_menu = None

    def width_center(self, image):
        width = self.screen.get_rect().width
        return (width / 2) - (image.get_width() / 2)

    def update(self, time):
        self.main_menu.update(time)