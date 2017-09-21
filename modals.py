import  game
import pygame

class Modals:

    def __init__(self, screen, resourcePath, tmpPath):
        self.resourcePath = resourcePath
        self.tmpPath = tmpPath
        self.screen = screen
        self.screen_size = screen.get_size()
        self.mosqito = pyxel.AnimatedPyxel(pyxel.Pyxel(self.resourcePath+'/gfx/Kłucie.pyxel', self.tmpPath))
        self.ass = pygame.image.load(self.resourcePath+"/gfx/pupa/PUPA_CIEŃ_pupa.png").convert_alpha()
        self.handshadow = pygame.image.load(self.resourcePath+"/gfx/pupa/PUPA_CIEŃ_reka cien.png").convert_alpha()
        self.fallenHand = pygame.image.load(self.resourcePath+"/gfx/pupa/PUPA_CIEŃ_reka wypelnienie.png").convert_alpha()
        self.hand_speed = 6
        self.hand_y = 400
        self.hand_x = 130
        self.hand_bounds = (100, 700)
        self.done = False
        self.fallOn = None
        self.drawShadow = True
        self.saved = None 
        self.goOn = 1000
        self.fallen = False
        self.finished = False
        self.finishCountdown = False
        self.finishTimeout = None
    def renderRun(self):
        #self.rect = pygame.draw.rect(self.screen, (0,0,0), self.getRect(), 0)
        self.screen.blit(self.ass, (60, 60))
        self.screen.blit(pygame.transform.scale(self.mosqito.current_image(), (64, 64)), (330, 550))
        if self.drawShadow:
            self.screen.blit(self.handshadow, (self.hand_x, self.hand_y))
        if self.time_remaining > 0:
            pygame.draw.rect(self.screen, (255,0,0), pygame.Rect((100, 100), (self.time_remaining*2, 20)), 0)
        if self.fallOn:
            if abs(self.hand_x - self.fallOn)<10:
                self.drawShadow = False
                self.hand_speed = 0
                self.screen.blit(self.fallenHand, (self.fallOn-100, 100))
                if not self.finishCountdown:
                    self.finishCountdown = True
                    self.finishTimeout = 100
                
        # run_view = pygame.image.load(self.resourcePath+"/gfx/runscreen.png").convert()

    def getRect(self):
        lu = (50, 50)

        return (lu, (self.screen_size[0] - 80, self.screen_size[1] - 80))
    def updateForTime(self, time):
        self.mosqito.update(time)
        if not self.hand_bounds[0] < self.hand_x < self.hand_bounds[1]:
            self.hand_speed *= -1
        self.hand_x += self.hand_speed*time
        if self.time_remaining <= 0:
            if self.saved:
                self.fallOn = 650
            else:
                self.fallOn = 270
        if self.finishCountdown:
            self.finishTimeout -= time
        if self.finishCountdown and self.finishTimeout <= 0:
            self.finished = True
    
            
import pyxel
