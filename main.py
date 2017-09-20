#!/usr/bin/env python3

import pygame
from characters.Mosquito import Mosquito
from characters.Bat import Bat
from characters.RaidBall import RaidBall
from menu import Menu, MenuItem
from viewport import Viewport
from game import Game
from score import Score
from modals import Modals
import sys
import random
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
bat.x = -500
bat.y = -300

mute = 0

def initApp():
    """Initialize app"""
    global screen, appAlive, clock, mainFont, bgImage, bgSize, fontTahoma, human
    pygame.init()
    pygame.display.set_caption("Blood Frenzy")
    pygame.mixer.init(44100, -16, 2, 2048)
    pygame.mixer.music.load('resources/sounds/buzz.mp3')

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
        pygame.K_2: False,
        pygame.K_q: False,
        pygame.K_p: False
    }

from characters.GasMask import GasMask  
def placeRandomBonus(): 
    bonus = GasMask() 
    bonus.x = random.randrange(-bgSize[0],0)
    bonus.y = random.randrange(-bgSize[1] + 384, 0)
    return bonus

def resetGame():
    global screen, viewport, score, mosquito, bat, mute

    score = Score(screen)
    bgImage = pygame.image.load("resources/gfx/tlo_ost_calosc.png").convert()
    bgSize = bgImage.get_size()
    boundariesX = (0, bgSize[0])
    boundariesY = (0, bgSize[1])

    mosquito = Mosquito()
    mosquito.x = 100
    mosquito.y = 100
    mosquito.score = score
    mosquito.set_boundaries(boundariesX, boundariesY)
    mosquito.image = pygame.image.load("resources/gfx/mosquito.png").convert_alpha()
    mosquito.empty_animation = pyxel.AnimatedPyxel(pyxel.Pyxel('resources/gfx/Latanie.pyxel', 'tmp'))
    mosquito.mid_animation = pyxel.AnimatedPyxel(pyxel.Pyxel('resources/gfx/Latanie_napełniony1.pyxel', 'tmp'))
    mosquito.full_animation = pyxel.AnimatedPyxel(pyxel.Pyxel('resources/gfx/Latanie_napełniony2.pyxel', 'tmp'))
    mosquito.suck_target = None

    bat = Bat()
    bat.x = -500
    bat.y = -300
    bat.animation = pyxel.AnimatedPyxel(pyxel.Pyxel('resources/gfx/Topesz_Latajuncy.pyxel', 'tmp'))

    mute = 0

    viewport = Viewport(bgImage, screen, mosquito, [bat])

keys_pressed = create_key_set()
TIME_MODIFIER = 0.2
initApp()
bonusCounter = random.randrange(1500, 4500)
pygame.joystick.init()

if pygame.joystick.get_count() and not 'no-joystick' in sys.argv:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    joystick = None

game = Game(screen)

game.main_menu = Menu(game, [
    MenuItem(Menu.ITEM_START, 285),
    MenuItem(Menu.ITEM_EXIT, 415),
    MenuItem(Menu.ITEM_CREDITS, 540)
])

game.restart_menu = Menu(game, [
    MenuItem(Menu.ITEM_RESTART, 285),
    MenuItem(Menu.ITEM_EXIT, 415),
    MenuItem(Menu.ITEM_CREDITS, 540)
])

score = Score(screen)
mosquito.score = score

gasMaskIcon = pygame.transform.scale(pygame.image.load("resources/gfx/maska gazowa.png").convert_alpha(), (64,64))
viewport = Viewport(bgImage, screen, mosquito, [bat])
last_keys_pressed = create_key_set()
if 'fullscreen' in sys.argv:
    pygame.display.toggle_fullscreen()
run_view = pygame.image.load("resources/gfx/runscreen.png").convert()
blood_bg = pygame.image.load("resources/gfx/Blood_LVL_Background.png").convert_alpha()
blood_fg = pygame.image.load("resources/gfx/Blood_LVL_Frame.png").convert_alpha()

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
        keys_pressed[pygame.K_q] = joystick.get_button(4)
        keys_pressed[pygame.K_p] = joystick.get_button(5)
        for key, pressed in keys_pressed.items():
            if pressed:
                if not last_keys_pressed[key]:
                    keys_down[key] = True
        last_keys_pressed = dict(keys_pressed)

    if game.scene == Game.SCENE_MENU:
        image = pygame.image.load('resources/gfx/START.jpg', 'tmp').convert()
        game.screen.blit(image, (0, 0))
        game.main_menu.handle_keys(keys_down)
        game.main_menu.update(time)
        game.main_menu.render()
    elif game.scene == Game.SCENE_CREDITS:
        image = pygame.image.load('resources/gfx/CREDITS.jpg', 'tmp').convert()
        game.screen.blit(image, (0, 0))
        if keys_down[pygame.K_RETURN]:
            game.scene = Game.SCENE_MENU
    elif game.scene == Game.SCENE_GAME_OVER:
        image = pygame.image.load('resources/gfx/game over.jpg', 'tmp').convert()
        game.screen.blit(image, (0, 0))
        game.restart_menu.handle_keys(keys_down)
        game.restart_menu.update(time)
        game.restart_menu.render()
        score.show_final_score()
    elif game.scene == Game.SCENE_RESTART:
        print('restart')
        resetGame()
        game.scene = Game.SCENE_GAME
    else:
        if mute == 0:
            pygame.mixer.music.play(-1)
            mute =1

        if not viewport.freeze:
            wasfrozen = False
            bonusCounter -= time
            if bonusCounter <= 0:
                bonusCounter = random.randrange(1500, 4500)
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

            # human.updateForTime(time)

            viewport.update(mosquito.x, mosquito.y)
            mosquito.updateForTime(time)
            bat.max_speed = 0.8+(score.score/1000) 
            bat.update_accelerations((mosquito.x, mosquito.y))
            suckable_in_range =list(filter(lambda x: x.suckable, viewport.collisions))
            if suckable_in_range:
                if mosquito.suck:
                    mosquito.suck = keys_pressed[pygame.K_SLASH]
                else:
                    mosquito.suck = keys_down[pygame.K_SLASH]
                    mosquito.suck_target = suckable_in_range[0] #suck from first suckable, whatever
            else:
                mosquito.suck = False
                mosquito.suck_target = None
                if len(list(filter(lambda x: x.unsuckable, viewport.collisions)))>0:
                    if mosquito.unsuck:
                        mosquito.unsuck = keys_pressed[pygame.K_SLASH]
                    else:
                        mosquito.unsuck = keys_down[pygame.K_SLASH]
                else:
                    mosquito.unsuck = False
            for killer in filter(lambda x: x.killer, viewport.collisions):
                pygame.mixer.music.stop()
                if isinstance(killer, Bat):
                    if not 'jebacnietopyra' in sys.argv:
                        print("ZAJEBOŁ CIE NETOPYR");
                        game.scene = Game.SCENE_GAME_OVER
                elif isinstance(killer, RaidBall):
                    if mosquito.hasGasMaskOn:
                        mosquito.hasGasMaskOn = False
                        viewport.enemies.remove(killer)
                    else:
                        print("ZAJEBOŁ CIE JOŁOP Z RAIDEM");
                        game.scene = Game.SCENE_GAME_OVER
            viewport.updateForTimeOnEnemies(time)
            viewport.draw()
            score.showScore()
            ###TODO poładnić
            game.screen.blit(blood_bg, (20,500))     
            pygame.draw.rect(screen, pygame.Color(255, 0, 0), (27, 695, 36, -mosquito.blood_percent * 1.9))
            game.screen.blit(blood_fg, (20,500))     
            if mosquito.hasGasMaskOn:
                game.screen.blit(gasMaskIcon, (10, 10))
        else:
            if not wasfrozen:
                viewport.modal = Modals(game.screen)
                viewport.modal.time_remaining = 400
            else:
                viewport.modal.time_remaining -= time
            if not viewport.modal.finished:
                viewport.draw()
                viewport.modal.updateForTime(time/3)
                viewport.modal.renderRun()
                # game.screen.blit(run_view, (0, 0))
                wasfrozen = True
                if viewport.modal.time_remaining > 0 and keys_pressed[pygame.K_q] and keys_pressed[pygame.K_p]:
                    if mosquito.suck_target in viewport.enemies:
                        viewport.enemies.remove(mosquito.suck_target)
                    viewport.modal.saved = True
                if viewport.modal.time_remaining < 0:
                    viewport.modal.saved = False
            else:
                viewport.freeze = False
            
        

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
