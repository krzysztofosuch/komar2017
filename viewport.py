import random
import itertools

from characters.Grill import Grill
from characters.Water import Water
from characters.Human import Human
from characters.Bat import Bat
from characters.Camping import Camping
from characters.Campfire import Campfire
from characters.Hollow import Hollow


class Viewport:
    order = [Campfire, Camping, Water, Human, Bat]

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

    def draw(self):
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

        mosquito_rect = self.mosquito.rect()
        abs_mosquito_rect = mosquito_rect.move(mosquitoX, mosquitoY)
        self.collisions = []

        # Render landscape
        for element in self.landscape_elements:
            self.screen.blit(element.current_image(), (bX - element.x, bY - element.y))

        # Check collisions, render enemies
        for enemy in sorted(self.enemies, key=lambda x: self.order.index(x.__class__)):
            enemy_position = (bX - enemy.x, bY - enemy.y)
            self.screen.blit(enemy.current_image(), enemy_position)
            abs_enemy_rect = enemy.rect().move(enemy_position)

            # Collision detection
            if abs_enemy_rect.colliderect(abs_mosquito_rect):
                self.collisions.append(enemy)

        self.screen.blit(self.mosquito.current_image(), (mosquitoX, mosquitoY))

    def addEnemy(self, enemy):
        self.enemies.append(enemy)

    def generate_landscape(self, background_index):
        mod_x = background_index * self.background_size[0]

        for _ in itertools.repeat(0, 1):
            camping = Camping()
            camping.x = random.randint(-self.background_size[0], 0) - mod_x
            camping.y = 510 - self.background_size[1]
            self.landscape_elements.append(camping)

        for _ in itertools.repeat(0, 1):
            campfire = Campfire()
            campfire.x = random.randint(-self.background_size[0], 0) - mod_x
            campfire.y = random.randint(150 - self.background_size[1], 360 - self.background_size[1])
            self.landscape_elements.append(campfire)

        for _ in itertools.repeat(0, 1):
            hollow = Hollow()
            add_x = random.randint(-5, 5)
            hollow.x = random.choice([-1075, -2310, -3157]) - mod_x + add_x
            hollow.y = random.randint(550 - self.background_size[1], 700 - self.background_size[1])
            self.landscape_elements.append(hollow)

        for _ in itertools.repeat(0, 1):
            grill = Grill()
            grill.x = random.randint(-self.background_size[0], 0) - mod_x
            grill.y = random.randint(150 - self.background_size[1], 360 - self.background_size[1])
            self.landscape_elements.append(grill)