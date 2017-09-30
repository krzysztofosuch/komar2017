import os
import pygame
import sys

from game import Game
from pyxel import Pyxel, AnimatedPyxel


class Menu:
    ITEM_START = 'Start Game'
    ITEM_EXIT = 'Exit'
    ITEM_CREDITS = 'Credits'
    ITEM_RESTART = 'Restart'

    def __init__(self, game, items, resourcePath, tmpPath):
        self.game = game
        self.current = 0
        pyxel = Pyxel(resourcePath+'/gfx/Topesz_Latajuncy.pyxel', tmpPath)
        self.pointer = AnimatedPyxel(pyxel)
        self.items = items

    def render(self):
        current_item = self.items[self.current]
        image = self.pointer.current_image()
        self.game.screen.blit(image, (380, current_item.y))
        self.game.screen.blit(image, (810, current_item.y))

    def update(self, time):
        self.pointer.update(time)

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
            if Menu.ITEM_CREDITS == item.name:
                self.game.scene = Game.SCENE_CREDITS
            if Menu.ITEM_RESTART == item.name:
                self.game.scene = Game.SCENE_RESTART
                #self.game.enabled = False
                print('changed scene')
                #raise Exception("Not implemmented")

        if self.current < 0:
            self.current = len(self.items) - 1

        if self.current > len(self.items) - 1:
            self.current = 0


class MenuItem:
    def __init__(self, name, y):
        self.name = name
        self.y = y
