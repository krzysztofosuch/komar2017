#!/usr/bin/env python3

import pygame
from characters.Mosquito import Mosquito
from characters.Human import Human
from characters.Water import Water
from viewport import Viewport
from menu import Menu
from game import Game
import sys
import random
from var_dump import var_dump
import pyxel
# GLOBALS
W_WIDTH = 1024
W_HEIGHT = 600

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = 0
clock = 0
mainFont = 0
fontTahoma = 0
xOffset = 0
yOffset = 0
mosquito = Mosquito()
mosquito.x = 100
mosquito.y = 100

human = 0
water = None
bgImage = 0


def initApp():
    """Initialize app"""
    global screen, appAlive, clock, mainFont, bgImage, fontTahoma, human
    pygame.init()
    pygame.display.set_caption("Blood Frenzy")
    fontTahoma = pygame.font.SysFont('Tahoma', 16, False, False)
    clock = pygame.time.Clock()
    mainFont = pygame.font.SysFont('Tahoma', 16, False, False)
    size = (W_WIDTH, W_HEIGHT)
    screen = pygame.display.set_mode(size)

    bgImage = pygame.image.load("resources/gfx/tlo_ost_calosc.png").convert()
    bgSize = bgImage.get_size()
    boundariesX = (0, bgSize[0])
    boundariesY = (0, bgSize[1])

    mosquito.set_boundaries(boundariesX, boundariesY)
    mosquito.image = pygame.image.load("resources/gfx/mosquito.png").convert_alpha()
    mosquito.empty_animation = pyxel.AnimatedPyxel(pyxel.Pyxel('resources/gfx/Latanie.pyxel', 'tmp'))
    mosquito.mid_animation = pyxel.AnimatedPyxel(pyxel.Pyxel('resources/gfx/Latanie_napełniony1.pyxel', 'tmp'))
    mosquito.full_animation = pyxel.AnimatedPyxel(pyxel.Pyxel('resources/gfx/Latanie_napełniony2.pyxel', 'tmp'))

    randX = random.randrange(-bgSize[0],0)
    randY = -bgSize[1] + random.randrange(260,280)

    human = Human(randX, randY)
    human.set_boundaries(boundariesX, boundariesY)
    human.animation =pyxel.AnimatedPyxel(pyxel.Pyxel('resources/gfx/Human1_walk.pyxel', 'tmp'))
    
    water.x = random.randrange(-bgSize[0],0)
    water.y = -bgSize[1] + random.randrange(260,280)
    water.image = pygame.image.load("resources/gfx/kałuża.png").convert_alpha()
    screen.fill(BLACK)
    pygame.display.flip()


def create_key_set():
    return {
        pygame.K_RIGHT: False,
        pygame.K_LEFT: False,
        pygame.K_UP: False,
        pygame.K_DOWN: False,
        pygame.K_RETURN: False,
        pygame.K_SLASH: False,
        pygame.K_GREATER: False
    }

water = Water()
keys_pressed = create_key_set()
TIME_MODIFIER = 0.2
initApp()

pygame.joystick.init()
if pygame.joystick.get_count() and not 'no-joystick' in sys.argv:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    joystick = None
game = Game(screen)
menu = Menu(game)

viewport = Viewport(bgImage, screen, mosquito, [human, water])
last_keys_pressed = create_key_set()
while game.enabled:
    screen.fill(BLACK)

    time = clock.get_time() * TIME_MODIFIER
    keys_down = create_key_set()

    #    print("Frame time: %s"%time)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.enabled = False
        elif event.type == pygame.KEYDOWN:
            if event.key in keys_pressed:
                keys_down[event.key] = True
            if event.key in keys_down:
                keys_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            if event.key in keys_pressed:
                keys_pressed[event.key] = False

    if joystick:
        keys_pressed[pygame.K_RIGHT] = joystick.get_axis(0) > 0.5
        keys_pressed[pygame.K_LEFT] =joystick.get_axis(0) < -0.5
        keys_pressed[pygame.K_DOWN] = joystick.get_axis(1) > 0.5
        keys_pressed[pygame.K_UP] =joystick.get_axis(1) < -0.5
        keys_pressed[pygame.K_RETURN] = joystick.get_button(9) or joystick.get_button(2)
        keys_pressed[pygame.K_SLASH] = joystick.get_button(7)
        keys_pressed[pygame.K_GREATER] = joystick.get_button(6) 
        for key, pressed in keys_pressed.items():
            if pressed:
                if not last_keys_pressed[key]:
                    keys_down[key] = True
        last_keys_pressed = dict(keys_pressed)

    if game.scene == Game.SCENE_MENU:
        menu.handle_keys(keys_down)
#        menu.update(time)
        menu.render()
    else:
        if keys_pressed[pygame.K_RIGHT]:
            mosquito.acc_x = 1
            mosquito.direction = True
        elif keys_pressed[pygame.K_LEFT]:
            mosquito.acc_x = -1
            mosquito.direction = False
        else:
            mosquito.acc_x = 0

        if keys_pressed[pygame.K_UP]:
            mosquito.acc_y = -1
        elif keys_pressed[pygame.K_DOWN]:
            mosquito.acc_y = 1
        else:
            mosquito.acc_y = 0

        human.updateForTime(time)

        viewport.update(mosquito.x, mosquito.y)
        mosquito.updateForTime(time)
        if len(list(filter(lambda x: x.suckable, viewport.collisions)))>0:
            if mosquito.suck:
                mosquito.suck = keys_pressed[pygame.K_SLASH]
            else:
                mosquito.suck = keys_down[pygame.K_SLASH]
        else:
            mosquito.suck = False
        
        if len(list(filter(lambda x: x.unsuckable, viewport.collisions)))>0:
            if mosquito.unsuck:
                mosquito.unsuck = keys_pressed[pygame.K_SLASH]
            else:
                mosquito.unsuck = keys_down[pygame.K_SLASH]
        else:
            mosquito.unsuck = False
        viewport.draw()
        pygame.draw.rect(screen, pygame.Color(255, 0, 0), (20, 500, 20, -mosquito.blood_percent * 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
