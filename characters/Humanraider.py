from characters.Character import Character

class Humanraider(Character):
    suckable = True
    cooldown=1000
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 0
        self.rest = 0
        self.remainingRest = 0

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
    def setDestination(self):
        self.rest = 0
        self.length = random.randrange(0, 1000)

        # if random.randrange(0,1) > 0.5:
        self.direction = -self.direction

        # print('length ', self.length,', direction', self.direction)

    def setRest(self):
        self.remainingRest = random.randrange(100,1000)
        self.rest = 1

    def current_image(self):
        animation = self.walk_animation
        image = animation.current_image()
        if self.direction == 1:
            image = pygame.transform.flip(image, True, False)
        elif self.direction == -1:
            image = pygame.transform.flip(image, False, False)
        return pygame.transform.scale2x(image)
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
            raidBall.speed_x = max(min(2, speed_x),-3)
            raidBall.speed_y = max(min(2, speed_y ),-3)
            raidBall.ttl = 80
            raidBall.animation = pyxel.AnimatedPyxel(pyxel.Pyxel('resources/gfx/raid/chmura raid.pyxel', 'tmp'))
            self.cooldown = 1000
            return raidBall
        else:
            return None #dont shoot this time
from characters.RaidBall import RaidBall
import random
import pyxel
import pygame
