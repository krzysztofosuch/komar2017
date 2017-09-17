from characters.Human import Human

class Humanraider(Human):
    cooldown=1000

    def updateForTime(self, time):
        self.speed_x = 0.2
        # self.x = self.x + self.speed_x * time

        if self.rest == 0:
            self.animation = 1
            if self.length > 0:
                self.x += time * self.speed_x * self.direction
                self.length -= time * self.speed_x
            else:
                self.setRest()

        elif self.rest == 1:
            self.animation = 0
            if self.remainingRest > 0:
                self.remainingRest -= time
            else:
                self.setDestination()

        if self.animation:
            self.walk_animation.update(time)
            self.scream_animation.update(time)
        if self.cooldown > 0:
            self.cooldown = max(self.cooldown-time, 0)
        # print('l:  ',self.length, ' r: ', self.rest, ' rr: ', self.remainingRest)

        # if self.x > self.x_bound[1]:
        #     self.x = 0
        #
        # if self.x < 0:
        #     self.x = self.x_bound[1]

        # print(self.x,' ', self.y)
    def fire_raid(self, target_position):
        x_diff = -target_position[0]-self.x
        y_diff = -target_position[1]-self.y
        multipliter = 0.01
        speed_x = x_diff*multipliter
        speed_y = y_diff*multipliter
        if -1 <= speed_y <= 1 and -1 <= speed_y <= 1:
            raidBall = RaidBall()
            raidBall.x = self.x
            raidBall.y = self.y
            raidBall.speed_x = max(min(1, speed_x),-1)
            raidBall.speed_y = max(min(1, speed_y ),-1)
            raidBall.ttl = 120
            raidBall.image = pygame.image.load("resources/gfx/raid/raid.png").convert_alpha()
            #raidBall.animation = pyxel.AnimatedPyxel(pyxel.Pyxel('resources/gfx/raid/chmura raid.pyxel', 'tmp'))
            self.cooldown = 1000
            return raidBall
        else:
            return None #dont shoot this time
from characters.RaidBall import RaidBall
import random
import pyxel
import pygame
