import  game
import pygame

class Modals:

    def __init__(self, screen):
        self.screen = screen
        self.screen_size = screen.get_size()
        self.mosqito = pyxel.AnimatedPyxel(pyxel.Pyxel('resources/gfx/Kłucie.pyxel', 'tmp'))
        self.ass = pygame.image.load("resources/gfx/pupa/PUPA_CIEŃ_pupa.png").convert()

    def renderRun(self):
        self.rect = pygame.draw.rect(self.screen, (0,0,0), self.getRect(), 0)
        self.screen.blit(self.ass, (60, 60))
        self.screen.blit(pygame.transform.scale(self.mosqito.current_image(), (64, 64)), (330, 550))
        # run_view = pygame.image.load("resources/gfx/runscreen.png").convert()

    def getRect(self):
        lu = (50, 50)

        return (lu, (self.screen_size[0] - 80, self.screen_size[1] - 80))
    def updateForTime(self, time):
        print(time)
        self.mosqito.update(time)
import pyxel
