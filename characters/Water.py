import pygame
from characters.Character import Character


class Water(Character):
    unsuckable = True

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/gfx/woda.png')