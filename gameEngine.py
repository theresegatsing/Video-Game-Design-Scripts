import pygame
from pygame import event
from vector import *
from drawable import Mobile
from drawable import Drawable

class GameEngine(object):
    def __init__(self):

        self.Luigi = Mobile(vec(0,0), pygame.image.load("C:/Users/gatsi/Box/winter 2026/video game design/Luigi.png").convert_alpha())

    def draw(self,surface):
        surface.fill((255,255,255))

        myFont = pygame.font.SysFont("Times New Roman", 14)
        Google = myFont.render("Google", False, (0,0,0))
        #screen.blit(Google, (400, 200))
        surface.blit(Google, (400, 200))

        #screen.blit(Luigi, (500, 300))
        self.Luigi.draw(surface)
    
    def handleEvent(self, event):
       
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.Luigi.velocity[0] = 20
                    elif event.key == pygame.K_LEFT:
                        self.Luigi.velocity[0] = -20
                    elif event.key  == pygame.K_UP:
                        self.Luigi.velocity[1] = -20
                    elif event.key == pygame.K_DOWN:
                        self.Luigi.velocity[1] = 20


                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.Luigi.velocity[0] = 0
                    elif event.key == pygame.K_LEFT:
                        self.Luigi.velocity[0] = 0
                    elif event.key == pygame.K_UP:
                        self.Luigi.velocity[1] = 0
                    elif event.key == pygame.K_DOWN:
                        self.Luigi.velocity[1] = 0

    def update(self, seconds):
        self.Luigi.update(seconds)