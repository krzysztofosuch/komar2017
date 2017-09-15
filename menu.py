import pygame
from pygame.math import Vector2


class Menu:
    def __init__(self, screen):
        self.screen = screen
        width = screen.get_rect().width
        font = pygame.font.SysFont('Tahoma', 14)

        self.items = []
        position_width = width / 2
        position_height = 100

        for label in ['Start Game', 'Exit']:
            rendered = font.render(label, 1, (255, 255, 255))
            vector = Vector2(position_width, position_height)
            self.items.append(MenuItem(vector, rendered))
            position_height += 100

    def render(self):
        for item in self.items:
            self.screen.blit(item.render, item.vector)


class MenuItem:
    def __init__(self, vector, rendered):
        self.vector = vector
        self.rendered = rendered
