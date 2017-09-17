import pygame
from pyxel import Pyxel


class Score:
    score = 0

    def __init__(self, screen):
        self.screen = screen
        self.screensize = screen.get_size()
        self.posX = self.screensize[0] - 100
        self.posY = 20

    def addPoints(self, points):
        self.score += points

    def showScore(self):
        font = pygame.font.SysFont('Tahoma', 14)
        string = 'SCORE ' + str(int(self.score)).zfill(4)
        image = font.render(string, 1, (0, 0, 0))
        self.screen.blit(image, (self.posX, self.posY))

    def show_final_score(self):
        font = pygame.font.SysFont('Curier', 80)
        string = str(int(self.score)).zfill(4)
        score_image = Pyxel('resources/gfx/Score.pyxel', 'tmp').get_layer_image(0)
        image = font.render(string, 1, (228, 130, 89))
        self.screen.blit(image, (650, 100))
        self.screen.blit(score_image, (450, 100))
