from characters.Character import Character

class Mosquito(Character):
    blood_percent = 0
    blood_sucking_speed = 0.1
    suck = False
    unsuck = False
    hasGasMaskOn = False
    def updateForTime(self, time):
        self.x = self.x + self.speed_x * time

        new_y = self.y + self.speed_y*time

        if self.y_bound[0] < new_y < self.y_bound[1]:
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
        self.empty_animation.update(time)
        self.mid_animation.update(time)
        self.full_animation.update(time)
        if self.suck:
            self.blood_percent += time*self.blood_sucking_speed
            self.blood_percent = min(self.blood_percent,100)
            if self.blood_percent < 100:
                self.score.addPoints(1*(time)/15)
                if getattr(self.suck_target, 'afterSuck', None) is not None:
                    self.suck_target.afterSuck(0.5*(time)/2)

                    if self.suck_target.anger >= 75:
                        print('snake!')
                        sixSense = pygame.image.load("resources/gfx/sixSense.png").convert()
                        self.screen.blit(sixSense, (self.x, self.y - 20))

            self.update_accelerations()
        if self.unsuck:
            self.blood_percent -= time*self.blood_sucking_speed
            self.blood_percent = max(self.blood_percent,0)
            if self.blood_percent > 0:
                self.score.addPoints(5*(time)/10)
            self.update_accelerations()

    def update_accelerations(self):
        self.acceleration = self.base_acceleration*(1.3-(self.blood_percent/100))
        self.deceleration = self.base_deceleration*(1.3-(self.blood_percent/100))

    def current_image(self):
        if self.blood_percent < 30:
            animation = self.empty_animation
        elif self.blood_percent < 70:
            animation = self.mid_animation
        else:
            animation = self.full_animation
        image = animation.current_image()
        if self.direction:
            image = pygame.transform.flip(image, True, False)
        return pygame.transform.scale2x(image)

import math
import pyxel
import pygame
