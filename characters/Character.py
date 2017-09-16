class Character:
    x = 0
    y = 0
    acc_x = 0
    acc_y = 0
    speed_x = 0
    speed_y = 0
    base_acceleration = 0.02
    base_deceleration = 0.01
    acceleration = 0.02
    deceleration = 0.01
    max_speed = 3
    direction = False

    def set_boundaries(self, x_bound, y_bound):
        self.x_bound = x_bound
        self.y_bound = y_bound

    def current_image(self):
        if self.animation:
            image = self.animation.current_image()
        else:
            image = self.image
        if self.direction:
            image = pygame.transform.flip(image, True, False)
        return pygame.transform.scale2x(image)


import math
import pyxel
import pygame
