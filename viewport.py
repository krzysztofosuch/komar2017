from pprint import pprint


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

        # Render background on right side
        if self.screen_size[0] + self.x > self.background_size[0]:
            self.screen.blit(self.background, (self.background_size[0] - self.x + centerX, bY))

        # Render background on left side
        if self.x - centerX < 0:
            self.screen.blit(self.background, (-self.background_size[0] - self.x + centerX, bY))

        # Render main background
        self.screen.blit(self.background, (bX, bY))

        mosquito_rect = self.mosquito.rect()
        abs_mosquito_rect = mosquito_rect.move(mosquitoX, mosquitoY)

        # Check collisions, render enemies
        for enemy in self.enemies:
            enemy_position = (bX - enemy.x, bY - enemy.y)
            self.screen.blit(enemy.current_image(), enemy_position)
            abs_enemy_rect = enemy.rect().move(enemy_position)

            if abs_enemy_rect.colliderect(abs_mosquito_rect):
                pass  # collision detected

        self.screen.blit(self.mosquito.current_image(), (mosquitoX, mosquitoY))
