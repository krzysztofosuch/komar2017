import pygame
from game import Game
from pyxel import Pyxel


class Menu:
    ITEM_START = 'Start Game'
    ITEM_EXIT = 'Exit'

    def __init__(self, game):
        self.game = game
        self.current = 0

        self.items = [
            MenuItem(Menu.ITEM_START, Pyxel('resources/gfx/Przycisk_start.pyxel', 'tmp')),
            MenuItem(Menu.ITEM_EXIT, Pyxel('resources/gfx/Przycisk_exit.pyxel', 'tmp'))
        ]

    def render(self):
        current_item = self.items[self.current]
        position_y = 100
        half_width = self.game.screen.get_rect().width / 2

        for item in self.items:
            if item == current_item:
                image = item.active()
            else:
                image = item.inactive()

            position_y += 100
            position_x = half_width - (image.get_width() / 2)

            self.game.screen.blit(image, (position_x, position_y))

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
    def __init__(self, name, pyxel):
        self.name = name
        self.pyxel = pyxel

    def active(self):
        return self.pyxel.get_tile_image(0, 0)

    def inactive(self):
        return self.pyxel.get_tile_image(0, 1)
