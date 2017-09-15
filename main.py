#!/usr/bin/env python3

import pygame
from characters.Mosquito import Mosquito
from level import Level
from menu import Menu
from game import Game
import sys
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
bgImage = 0


def initApp():
    """Initialize app"""
    global screen, appAlive, clock, mainFont, bgImage, fontTahoma
    pygame.init()
    pygame.display.set_caption("Blood Frenzy")
    fontTahoma = pygame.font.SysFont('Tahoma', 16, False, False)
    clock = pygame.time.Clock()
    mainFont = pygame.font.SysFont('Tahoma', 16, False, False)
    size = (W_WIDTH, W_HEIGHT)
    screen = pygame.display.set_mode(size)
    bgImage = pygame.image.load("resources/gfx/background.png").convert()
    mosquito.image = pygame.image.load("resources/gfx/mosquito.png").convert_alpha()
    screen.fill(BLACK)
    screen.blit(bgImage, (0, 0))
    pygame.display.flip()


def create_key_set():
    return {
        pygame.K_RIGHT: False,
        pygame.K_LEFT: False,
        pygame.K_UP: False,
        pygame.K_DOWN: False,
        pygame.K_RETURN: False
    }

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

level = Level(bgImage, screen, (mosquito.x, mosquito.y))
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

    if game.scene == Game.SCENE_MENU:
        menu.handle_keys(keys_down)
        menu.render()
    else:
        if keys_pressed[pygame.K_RIGHT]:
            mosquito.acc_x = 1
        elif keys_pressed[pygame.K_LEFT]:
            mosquito.acc_x = -1
        else:
            mosquito.acc_x = 0

        if keys_pressed[pygame.K_UP]:
            mosquito.acc_y = -1
        elif keys_pressed[pygame.K_DOWN]:
            mosquito.acc_y = 1
        else:
            mosquito.acc_y = 0
        mosquito.updateForTime(time)
        level.update(-mosquito.acc_x, -mosquito.acc_y)
        level.draw()
        screen.blit(mosquito.image, (W_WIDTH / 2, W_HEIGHT / 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
