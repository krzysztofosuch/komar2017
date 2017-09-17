from characters.Powerup import Powerup
import pygame
class GasMask(Powerup):
    def __init__(self):
        self.image = pygame.image.load("resources/gfx/maska gazowa.png").convert_alpha()
 
