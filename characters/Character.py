class Character:
    x = 0
    y = 0
    acc_x = 0
    acc_y = 0
    speed_x = 0
    speed_y = 0
    acceleration = 0.01
    deceleration = 0.01
    max_speed = 2
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
        return image


import math
import pyxel
import pygame