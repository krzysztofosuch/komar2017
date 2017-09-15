#!/usr/bin/env python3

import pygame, time
from characters.Mosquito import Mosquito
# GLOBALS
W_WIDTH = 640
W_HEIGHT = 480

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
appAlive = False
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
    screen.fill(BLACK)
    screen.blit(bgImage, (0,0))
    pygame.display.flip()
    appAlive = True

colors = [BLACK, WHITE, RED, GREEN, BLUE]
colorLength = len(colors)
colorIndex = 0

initApp()

while appAlive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            appAlive = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                mosquito.acc_x = 10
            if event.key == pygame.K_LEFT:
                mosquito.acc_x = -10
            if event.key == pygame.K_UP:
                mosquito.acc_y = 10
            if event.key == pygame.K_DOWN:
                mosquito.acc_y = -10
        mosquito.updateForTime()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                colorIndex += 1
                if colorIndex > colorLength - 1:
                    colorIndex = 0
                xOffset = 10
                yOffset = 10
                screen.fill(colors[colorIndex])

            if event.key == pygame.K_LEFT:
                colorIndex -= 1
                if colorIndex < 0:
                    colorIndex = colorLength - 1
                xOffset = 10
                yOffset = 10
                screen.fill(colors[colorIndex])

            if event.key == pygame.K_DOWN:
                pygame.draw.line(screen, colors[colorIndex + 1], [0, yOffset], [W_WIDTH, yOffset], 2)
                yOffset += 10
                if yOffset >= W_HEIGHT:
                    yOffset = 10

            if event.key == pygame.K_UP:
                pygame.draw.line(screen, colors[colorIndex + 1], [xOffset, 0], [xOffset, W_HEIGHT], 2)
                xOffset += 10
                if xOffset >= W_WIDTH:
                    xOffset = 10

            if event.key == pygame.K_d:
                while xOffset < W_WIDTH and yOffset < W_HEIGHT:
                    pygame.draw.line(screen, colors[colorIndex + 1], [0, yOffset], [W_WIDTH, yOffset], 2)
                    pygame.display.flip()
                    pygame.draw.line(screen, colors[colorIndex + 1], [xOffset, 0], [xOffset, W_HEIGHT], 2)
                    pygame.display.flip()
                    yOffset += 10
                    xOffset += 10

        #InfoText = fontTahoma.render("DBG: Y: " + str(yOffset) + " X: " + str(xOffset), True, BLACK)
        # screen.blit(InfoText, [W_WIDTH - 132, W_HEIGHT - 30])
        
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
