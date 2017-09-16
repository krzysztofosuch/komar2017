import pygame
import pyxel
from game import Game


class Menu:
    ITEM_START = 'Start Game'
    ITEM_EXIT = 'Exit'

    def __init__(self, game):
        self.game = game
        self.current = 0
        width = game.screen.get_rect().width
        font = pygame.font.SysFont('Tahoma', 14)

        self.items = []
        half_width = width / 2
        position_height = 100

        for name in [Menu.ITEM_START, Menu.ITEM_EXIT]:
            image = font.render(name, 1, (255, 255, 255))
            position_width = half_width - (image.get_width() / 2)
            vector = (position_width, position_height)
            self.items.append(MenuItem(name, vector, image))
            position_height += 100

#        mosquito_pyxel = pyxel.Pyxel('resources/gfx/Latanie.pyxel', 'tmp')
#        self.mosquito = pyxel.AnimatedPyxel(mosquito_pyxel)

#    def update(self, time):
#        self.mosquito.update(time)

    def render(self):
        for item in self.items:
            self.game.screen.blit(item.rendered, item.vector)

        height = (self.current + 1) * 100
        height += 20
        item = self.items[self.current]
        vector_start = (item.vector[0], height)
        vector_end = (item.vector[0] + item.rendered.get_width(), height)
        pygame.draw.line(self.game.screen, (255, 255, 255), vector_start, vector_end, 1)

#        image = self.mosquito.current_image()
#        self.game.screen.blit(image, (self.game.width_center(image), 70))


    def handle_keys(self, keys):
        item = self.items[self.current]

        if keys[pygame.K_UP]:
            self.current -= 1

        if keys[pygame.K_DOWN]:
            self.current += 1

        if keys[pygame.K_RETURN]:
            if Menu.ITEM_START == item.name:
                self.game.scene = Game.SCENE_GAME
            if Menu.ITEM_EXIT == item.name:
                self.game.enabled = False

        if self.current < 0:
            self.current = len(self.items) - 1

        if self.current > len(self.items) - 1:
            self.current = 0


class MenuItem:
    def __init__(self, name, vector, rendered):
        self.name = name
        self.vector = vector
        self.rendered = rendered
