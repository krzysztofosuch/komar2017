import  game
import pygame

class Modals:

    def __init__(self, screen):
        self.screen = screen
        self.screen_size = screen.get_size()


    def renderRun(self):
        rect = pygame.draw.rect(self.screen, (0,0,0), self.getRect(), 0)
        print(self.getRect())
        ass = pygame.image.load("resources/gfx/pupa/PUPA_CIEŃ_pupa.png").convert()
        self.rect.blit(ass, (100, 100))
        # run_view = pygame.image.load("resources/gfx/runscreen.png").convert()

    def getRect(self):
        lu = (100, 100)

        return (lu, (self.screen_size[0] - 200, self.screen_size[1] - 200))
