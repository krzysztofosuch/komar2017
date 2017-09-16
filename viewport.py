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
        self.bg_instances = dict()
        self.collisions = []

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

        for mod in [-1, 0, 1]:
            index = bg_current_index + mod
            background_x = index * self.background_size[0] - self.x + centerX
            self.screen.blit(self.background, (background_x, bY))

        mosquito_rect = self.mosquito.rect()
        abs_mosquito_rect = mosquito_rect.move(mosquitoX, mosquitoY)
        self.collisions = []

        # Check collisions, render enemies
        for enemy in self.enemies:
            enemy_position = (bX - enemy.x, bY - enemy.y)
            self.screen.blit(enemy.current_image(), enemy_position)
            abs_enemy_rect = enemy.rect().move(enemy_position)
            if abs_enemy_rect.colliderect(abs_mosquito_rect):
                self.collisions.append(enemy)
        
        self.screen.blit(self.mosquito.current_image(), (mosquitoX, mosquitoY))
