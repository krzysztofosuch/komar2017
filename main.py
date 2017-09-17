#!/usr/bin/env python3

import pygame
from characters.Mosquito import Mosquito
from characters.Human import Human
from characters.Humanraider import Humanraider
from characters.Water import Water
from characters.Bat import Bat
from viewport import Viewport
from menu import Menu
from game import Game
from score import Score
import sys
import random
from var_dump import var_dump
import pyxel
# GLOBALS
W_WIDTH = 1280
W_HEIGHT = 800

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

bgImage = 0
bgSize = 0

mosquito = Mosquito()
mosquito.x = 100
mosquito.y = 100
bat = Bat()
bat.x = -300
bat.y = -300
human = 0
water = 0


def initApp():
    """Initialize app"""
    global screen, appAlive, clock, mainFont, bgImage, bgSize, fontTahoma, human
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

    bat.animation = pyxel.AnimatedPyxel(pyxel.Pyxel('resources/gfx/Topesz_Latajuncy.pyxel', 'tmp'))
    randX = random.randrange(-bgSize[0],0)
    randY = -bgSize[1] + random.randrange(260,280)

    human = Human(randX, randY)
    human.set_boundaries(boundariesX, boundariesY)
    human.walk_animation =pyxel.AnimatedPyxel(pyxel.Pyxel('resources/gfx/human1/Human_w.pyxel', 'tmp'))
    human.scream_animation =pyxel.AnimatedPyxel(pyxel.Pyxel('resources/gfx/human1/Human_s.pyxel', 'tmp'))

    water.x = random.randrange(-bgSize[0],0)
    water.y = -bgSize[1] + 384
    water.image = pygame.image.load("resources/gfx/woda.png").convert_alpha()
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
        pygame.K_GREATER: False,
        pygame.K_1: False,
        pygame.K_2: False
    }

def createHuman(viewport):
    randX = random.randrange(-bgSize[0], 0)
    randY = -bgSize[1] + random.randrange(260, 280)
    boundariesX = (0, bgSize[0])
    boundariesY = (0, bgSize[1])

    skin = random.randrange(1,5)

    walkAnimation = 'resources/gfx/human' + str(skin) + '/Human_w.pyxel'
    screamAnimation = 'resources/gfx/human' + str(skin) + '/Human_s.pyxel'

    human = Human(randX, randY)
    human.set_boundaries(boundariesX, boundariesY)
    human.walk_animation = pyxel.AnimatedPyxel(pyxel.Pyxel(walkAnimation, 'tmp'))
    human.scream_animation = pyxel.AnimatedPyxel(pyxel.Pyxel(screamAnimation, 'tmp'))

    viewport.addEnemy(human)

def createPuddle(viewport):
    water = Water()
    water.x = random.randrange(-bgSize[0], 0)
    water.y = -bgSize[1] + 384
    water.image = pygame.image.load("resources/gfx/woda.png").convert_alpha()
    viewport.addEnemy(water)
def createHumanraider(viewport):
    randX = random.randrange(-bgSize[0], 0)
    randY = -bgSize[1] + random.randrange(260, 280)
    boundariesX = (0, bgSize[0])
    boundariesY = (0, bgSize[1])

    skin = random.randrange(1,5)

    walkAnimation = 'resources/gfx/humanraider/Human_w.pyxel'
    screamAnimation = 'resources/gfx/humanraider/Human_s.pyxel'

    humanraider = Humanraider(randX, randY)
    humanraider.set_boundaries(boundariesX, boundariesY)
    humanraider.walk_animation = pyxel.AnimatedPyxel(pyxel.Pyxel(walkAnimation, 'tmp'))
    humanraider.scream_animation = pyxel.AnimatedPyxel(pyxel.Pyxel(screamAnimation, 'tmp'))
    viewport.addEnemy(humanraider)
from characters.GasMask import GasMask  
def placeRandomBonus(): 
    bonus = GasMask() 
    bonus.x = random.randrange(-bgSize[0],0)
    bonus.y = random.randrange(-bgSize[1] + 384, 0)
    print("PREZENT NA %s:%s"%(bonus.x, bonus.y))
    return bonus
water = Water()
keys_pressed = create_key_set()
TIME_MODIFIER = 0.2
initApp()
bonusCounter = random.randrange(100, 2000)
pygame.joystick.init()
if pygame.joystick.get_count() and not 'no-joystick' in sys.argv:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    joystick = None
game = Game(screen)
menu = Menu(game)
score = Score(screen)
mosquito.score = score

viewport = Viewport(bgImage, screen, mosquito, [human, water, bat])
last_keys_pressed = create_key_set()
if 'fullscreen' in sys.argv:
    pygame.display.toggle_fullscreen()
pygame.mouse.set_visible(False)
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
        menu.render()
    elif game.scene == Game.SCENE_CREDITS:
        pass
    elif game.scene == Game.SCENE_GAME_OVER:
        image = pygame.image.load('resources/gfx/game over.jpg', 'tmp')
        game.screen.blit(image, (0, 0))
    else:
        bonusCounter -= time
        if bonusCounter <= 0:
            bonusCounter = random.randrange(100, 2000)
            viewport.addEnemy(placeRandomBonus())
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

        if keys_down[pygame.K_1]:
            if random.choice([True,False]):
                createHuman(viewport)
            else:
                createHumanraider(viewport)

        if keys_down[pygame.K_2]:
            createPuddle(viewport)

        # human.updateForTime(time)

        viewport.update(mosquito.x, mosquito.y)
        mosquito.updateForTime(time)
        bat.update_accelerations((mosquito.x, mosquito.y))
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
        if not 'jebacnietopyra' in sys.argv:
            if len(list(filter(lambda x: x.killer, viewport.collisions)))>0:
                print("ZAJEBOŁ CIE NETOPYR");
                game.scene = Game.SCENE_GAME_OVER

        viewport.updateForTimeOnEnemies(time)
        viewport.draw()
        score.showScore()
        pygame.draw.rect(screen, pygame.Color(255, 0, 0), (20, 500, 20, -mosquito.blood_percent * 2))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
