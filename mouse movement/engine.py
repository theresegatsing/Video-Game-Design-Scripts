import pygame
from drawable import Drawable
from mobile import Mobile, Player
from os.path import join
from vector import vec, pyVec
from constants import *


class GameEngine(object):

    def __init__(self):        
        self.kirby = Player((0,0), "kirby.png", pygame.Rect(0,0,16,16), colorkey=True)
        self.background = Drawable((0,0), "background.png")
        self.waterLily = Drawable((250,100), "water-lily.png")
        self.rose = Drawable((100,100), "rose.png", pygame.Rect(4*34,0,34,62), transparency=True)
        self.carrot = Drawable((150,100), "plants.png", pygame.Rect(1,650,62,78), transparency=True)        
        self.subRainbow = Drawable((150,50), "rainbow.png", pygame.Rect(50,50,50,50))
        self.hoverRaibow = Drawable((150,50), "rainbow.png", pygame.Rect(100,100,50,50))
        self.drawRainbow = self.subRainbow
        self.kirbySpeed = 100

        self.collidables = [self.subRainbow, self.waterLily]

        #pygame.mouse.set_visible(False)

        self.dragged = None
        self.mouseOffset = vec(0,0)
    
    def draw(self, drawSurface):
        drawSurface.fill((255,255,255))
        
        self.background.draw(drawSurface)
        self.waterLily.draw(drawSurface)
        self.rose.draw(drawSurface)
        self.carrot.draw(drawSurface)
        self.subRainbow.draw(drawSurface)
        
        self.kirby.draw(drawSurface)
            
    def handleEvent(self, event):        
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = vec(*event.pos) // SCALE
            if self.kirby.getCollisionRect().collidepoint(position):
                self.dragged = self.kirby
                self.mouseOffset = self.kirby.getPosition() - position
            #self.kirby.position = position
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragged = None
        elif event.type == pygame.MOUSEMOTION:
            position = vec(*event.pos) // SCALE
            if self.dragged:
                self.dragged.position = position + self.mouseOffset

            if self.subRainbow.getCollisionRect().collidepoint(position):
                self.drawRainbow = self.hoverRaibow
            else:
                self.drawRainbow = self.subRainbow
            
        #elif event.type == pygame.MOUSEMOTION:
        #    position = vec(*event.pos) // SCALE
        #    self.subRainbow.position = position
        self.kirby.handleEvent(event)        
    
    def update(self, seconds):
        self.kirby.update(seconds)

        if self.kirby.getPosition()[0] <= 0:
            self.kirby.velocity[0] = 0
            self.kirby.position[0] = 0
        
        elif self.kirby.getPosition()[0] + self.kirby.getWidth() > RESOLUTION[0]:
            self.kirby.position[0] = RESOLUTION[0] - self.kirby.getWidth() 
            self.kirby.velocity[0]= 0
        
        if self.kirby.getPosition()[1] <= 0:
            self.kirby.velocity[1] = 0
            self.kirby.position[1] = 0
        elif self.kirby.getPosition()[1] + self.kirby.getHeight() > RESOLUTION[1]:
            self.kirby.position[1] = RESOLUTION[1] - self.kirby.getHeight()
            self.kirby.velocity[1]= 0


        for c in self.collidables:
            collision = self.kirby.getCollisionRect().clip(c.getCollisionRect())

            if collision.width !=0 and collision.height !=0:

                if collision.width  < collision.height:
                    #left /right push
                    self.kirby.velocity[0] = 0
                    if self.kirby.getPosition()[0] < c.getPosition()[0]:
                        #left push
                        
                        self.kirby.position[0] -= collision.width
                    else:
                        #right push
                        
                        self.kirby.position[0] += collision.width
                else:
                    self.kirby.velocity[1] = 0

                    if self.kirby.getPosition()[1] < c.getPosition()[1]:
                        #top push
                        
                        self.kirby.position[1] -= collision.height
                    else:
                        #bottom push
                        
                        self.kirby.position[1] += collision.height