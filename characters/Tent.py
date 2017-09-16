import pygame
from characters.Character import Character


class Tent(Character):
    unsuckable = True

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/gfx/namiot_boks.png')
