import pygame

from characters.Character import Character

class Bat(Character):
    killer = True
    max_speed = 0.4
    def updateForTime(self, time):
        self.x = self.x + self.speed_x * time
        new_y = self.y + self.speed_y*time
        self.y = new_y

        if self.acc_x != 0:
            self.speed_x = max(min(self.speed_x+(self.acceleration*time*self.acc_x), self.max_speed), -self.max_speed)
        else:
            if self.speed_x > 0:
                self.speed_x -= self.deceleration*time
            else:
                self.speed_x += self.deceleration*time
        if self.acc_y != 0:
            self.speed_y = max(min(self.speed_y+(self.acceleration*time*self.acc_y), self.max_speed), -self.max_speed)
        else:
            if self.speed_y > 0:
                self.speed_y -= self.deceleration*time
            else:
                self.speed_y += self.deceleration*time
        self.animation.update(time)

    def update_accelerations(self, target_position):
        x_diff = -target_position[0]-self.x
        y_diff = -target_position[1]-self.y
        multiplier = 0.25
        self.acc_x = x_diff*multiplier
        self.acc_y = y_diff*multiplier

    def rect_for_collision(self):
        return pygame.Rect((35, 35), (80, 80))
