import random
import itertools
import pygame

from characters.Powerup import Powerup
from characters.Grill import Grill
from characters.Water import Water
from characters.Human import Human
from characters.Bat import Bat
from characters.Camping import Camping
from characters.Campfire import Campfire
from characters.Hollow import Hollow
from characters.Humanraider import Humanraider
from characters.RaidBall import RaidBall
from characters.GasMask import GasMask
from pyxel import AnimatedPyxel, Pyxel


class Viewport:
    freeze = False
    order = [Water, Campfire, Camping, Grill, Hollow, Human, Humanraider, GasMask, Bat, RaidBall]

    def __init__(self, background, screen, mosquito, enemies):
        self.x = mosquito.x
        self.y = mosquito.y
        self.background = background
        self.screen = screen
        self.screen_size = screen.get_size()
        self.background_size = background.get_size()
        self.mosquito = mosquito
        self.mosquitoSize = self.mosquito.image.get_size()
        self.enemies = enemies
        self.collisions = []
        self.generated_screens = []
        self.landscape_elements = []

    def update(self, x, y):
        self.x = x - (self.mosquitoSize[0] / 2)
        self.y = y - (self.mosquitoSize[1] / 2)

    def randomlyPlacePowerup(self):
        pass    

    def draw(self):
        self.randomlyPlacePowerup()
        centerX = self.screen_size[0] / 2
        centerY = self.screen_size[1] / 2
        maxY = self.screen_size[1]
        maxMosquitoY = self.background.get_size()[1]
        mosquitoX = centerX
        bX = -self.x + centerX

        if self.y < centerY:
            mosquitoY = self.y
            bY = 0
        elif self.y < maxMosquitoY - centerY:
            mosquitoY = centerY
            bY = -self.y + centerY
        else:
            mosquitoY = centerY + (centerY - (maxMosquitoY - self.y))
            bY = -maxMosquitoY + maxY

        bg_current_index = int(self.x / self.background_size[0])

        for mod in [-2, -1, 0, 1]:
            index = bg_current_index + mod
            background_x = index * self.background_size[0] - self.x + centerX
            self.screen.blit(self.background, (background_x, bY))

            # Generating new items on new screen
            if index not in self.generated_screens:
                self.generate_landscape(index)
                self.generated_screens.append(index)

        mosquito_rect = self.mosquito.rect_for_collision()
        abs_mosquito_rect = mosquito_rect.move(mosquitoX, mosquitoY)
        self.collisions = []
        # pygame.draw.rect(self.screen, (255, 0, 0), abs_mosquito_rect, 1)

        # Check collisions, render enemies (or landscape)
        for enemy in sorted(self.enemies, key=lambda x: self.order.index(x.__class__)):
            enemy_position = (bX - enemy.x, bY - enemy.y)
            self.screen.blit(enemy.current_image(), enemy_position)
            abs_enemy_rect = enemy.rect_for_collision().move(enemy_position)
            if isinstance(enemy, Human):
                #pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect((enemy_position[0], enemy_position[1]), (15, enemy.anger) ))
                if enemy.anger > 100:
                    enemy.anger = 0
                    self.freeze = True 
            # Collision detection
            if abs_enemy_rect.colliderect(abs_mosquito_rect):
                if isinstance(enemy, Powerup):
                    enemy.applyToCharacter(self.mosquito) 
                    self.enemies.remove(enemy)
                else:
                    self.collisions.append(enemy)
                    
        self.screen.blit(self.mosquito.current_image(), (mosquitoX, mosquitoY))
        if getattr(self.mosquito.suck_target, 'afterSuck', None) is not None:
            if self.mosquito.suck_target.anger >= 75:
                sixSense = pygame.image.load("resources/gfx/wykrzyknik.png")
                self.screen.blit(sixSense, (mosquitoX + 20, mosquitoY - 30))

    def addEnemy(self, enemy):
        self.enemies.append(enemy)

    def generate_landscape(self, background_index):
        mod_x = background_index * self.background_size[0]

        for _ in itertools.repeat(0, 1):
            camping = Camping()
            camping.x = random.randint(-self.background_size[0], 0) - mod_x
            camping.y = 510 - self.background_size[1]
            self.enemies.append(camping)

        for _ in itertools.repeat(0, 1):
            campfire = Campfire()
            campfire.x = random.randint(-self.background_size[0], 0) - mod_x
            campfire.y = random.randint(150 - self.background_size[1], 360 - self.background_size[1])
            self.enemies.append(campfire)

        for _ in itertools.repeat(0, 1):
            hollow = Hollow()
            add_x = random.randint(-5, 5)
            hollow.x = random.choice([-1075, -2310, -3157]) - mod_x + add_x
            hollow.y = random.randint(550 - self.background_size[1], 700 - self.background_size[1])
            self.enemies.append(hollow)

        for _ in itertools.repeat(0, 1):
            grill = Grill()
            grill.x = random.randint(-self.background_size[0], 0) - mod_x
            grill.y = random.randint(150 - self.background_size[1], 360 - self.background_size[1])
            self.enemies.append(grill)

        for _ in itertools.repeat(0, random.randint(0, 3)):
            position_x = random.randint(-self.background_size[0], 0) - mod_x
            position_y = random.randint(260 - self.background_size[1], 280 - self.background_size[1])

            boundaries_x = (position_x - self.background_size[0], position_x + self.background_size[0])
            boundaries_y = (0, position_y)

            skin = random.randrange(1, 5)

            if 1 == random.randrange(1, 10):
                human = Humanraider(position_x, position_y)
                walk_animation = 'resources/gfx/humanraider/Human_w.pyxel'
                scream_animation = 'resources/gfx/humanraider/Human_s.pyxel'
            else:
                human = Human(position_x, position_y)
                walk_animation = 'resources/gfx/human' + str(skin) + '/Human_w.pyxel'
                scream_animation = 'resources/gfx/human' + str(skin) + '/Human_s.pyxel'

            human.set_boundaries(boundaries_x, boundaries_y)
            human.walk_animation = AnimatedPyxel(Pyxel(walk_animation, 'tmp'))
            human.scream_animation = AnimatedPyxel(Pyxel(scream_animation, 'tmp'))

            self.enemies.append(human)

        for _ in itertools.repeat(0, 1):
            water = Water()
            water.x = random.randint(-self.background_size[0], 0) - mod_x
            water.y = 384 - self.background_size[1]
            self.enemies.append(water)


    def updateForTimeOnEnemies(self, time):
        for enemy in self.enemies:
            enemy.updateForTime(time)
            if getattr(enemy, 'ttl', None) is not None and enemy.ttl <= 0:
                self.enemies.remove(enemy)
            if isinstance(enemy, Humanraider):
                if enemy.cooldown <= 0:
                    ball = enemy.fire_raid((self.mosquito.x, self.mosquito.y))
                    if ball:
                        self.addEnemy(ball)
