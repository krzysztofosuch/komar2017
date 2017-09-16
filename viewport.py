import random
import itertools
from characters.Tent import Tent


class Viewport:
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
        for enemy in self.enemies:
            enemy_position = (bX - enemy.x, bY - enemy.y)
            self.screen.blit(enemy.current_image(), enemy_position)
            abs_enemy_rect = enemy.rect().move(enemy_position)

            # Collision detection
            if abs_enemy_rect.colliderect(abs_mosquito_rect):
                self.collisions.append(enemy)
        
        self.screen.blit(self.mosquito.current_image(), (mosquitoX, mosquitoY))

    def generate_landscape(self, background_index):
        mod_x = background_index * self.background_size[0]

        for _ in itertools.repeat(0, 1):
            tent = Tent()
            tent.x = random.randint(-self.background_size[0], 0) - mod_x
            tent.y = random.randint(150-self.background_size[1], 300 - self.background_size[1])
            self.landscape_elements.append(tent)
