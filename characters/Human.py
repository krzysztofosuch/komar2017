from characters.Character import Character

class Human(Character):
    suckable = True
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def updateForTime(self, time):
        if self.animation:
            self.animation.update(time)

import math
import pyxel
import pygame
