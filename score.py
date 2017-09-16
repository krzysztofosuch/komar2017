import pygame
from game import Game
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