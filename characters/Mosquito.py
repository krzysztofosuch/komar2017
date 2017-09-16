class Mosquito:
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
    def updateForTime(self, time):
        new_x = self.x + self.speed_x*time
        if new_x > self.x_bound[0] and new_x < self.x_bound[1]:
            self.x = new_x
        else:
            if new_x < self.x_bound[0]:
                new_x = self.x_bound[0]+2
            else:
                new_x = self.x_bound[1]-2
            self.x = new_x
            self.acc_x = -self.acc_x
            self.speed_x = -self.speed_x
        new_y = self.y + self.speed_y*time
        if new_y > self.y_bound[0] and new_y < self.y_bound[1]:
            self.y = new_y
        else:
            if new_y < self.y_bound[0]:
                new_y = self.y_bound[0]+2
            else:
                new_y = self.y_bound[1]-2
            self.y = new_y
            self.acc_y = -self.acc_y
            self.speed_y = -self.speed_y


        if self.acc_x != 0:
            self.speed_x = min(self.speed_x+(self.acceleration*time*self.acc_x), self.max_speed)
        else:
            if self.speed_x > 0:
                self.speed_x -= self.deceleration*time
            else:
                self.speed_x += self.deceleration*time
        if self.acc_y != 0:
            self.speed_y = min(self.speed_y+(self.acceleration*time*self.acc_y), self.max_speed)
        else:
            if self.speed_y > 0:
                self.speed_y -= self.deceleration*time
            else:
                self.speed_y += self.deceleration*time
        if self.animation:
            self.animation.update(time)

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
