from characters.Character import Character

class Human(Character):
    def __init__(self, x, y):
        print(x)
        print(y)
        self.x = x
        self.y = y
        self.length = 0
        self.rest = 0
        self.remainingRest = 0

    def updateForTime(self, time):
        self.speed_x = 1
        # self.x = self.x + self.speed_x * time

        if self.length == 0 and self.rest == 0:
            self.setRest()

        if self.length == 0 and self.rest == 1:
            self.remainingRest -= time

        if self.length == 0 and self.rest == 1 and self.remainingRest == 0:
            self.setDestination()

        if self.length != 0 and self.rest == 0:
            self.x += time * self.speed_x * self.direction
            self.length -= time * self.speed_x




        # if self.x > self.x_bound[1]:
        #     self.x = 0
        #
        # if self.x < 0:
        #     self.x = self.x_bound[1]



        if self.animation:
            self.animation.update(time)

        print(self.x,' ', self.y)

    def setDestination(self):
        self.length = random.randrange(0, bgSize[0])/10

        if random.randrange(0,1):
            self.direction = -self.direction

        print('length ', self.length,', direction', self.direction)

    def setRest(self):
        self.remainingRest = random.randrange(2,12)
        self.rest = 1


import random
import pyxel
import pygame
