import pygame
from drawable import Drawable
from mobile import Mobile, Player
from os.path import join
from vector import vec, pyVec
from constants import *
from animated import Animated
import random 

class GameEngine(object):

    def __init__(self):        
        self.kirby = Player((0,0), "kirby.png",  (1,0))
        self.kirby.animate = True
        self.background = Drawable((0,0), "background.png")
        self.waterLily = Drawable((250,100), "water-lily.png")
        self.rose = Drawable((100,100), "rose.png", pygame.Rect(4*34,0,34,62))
        self.carrot = Drawable((150,100), "plants.png", pygame.Rect(1,650,62,78))        
        self.subRainbow = Drawable((150,50), "rainbow.png", pygame.Rect(50,50,50,50))
        self.hoverRaibow = Drawable((150,50), "rainbow.png", pygame.Rect(100,100,50,50))
        self.drawRainbow = self.subRainbow
        self.kirbySpeed = 100

        self.collidables = [self.subRainbow, self.waterLily]

        #pygame.mouse.set_visible(False)

        self.dragged = None
        self.mouseOffset = vec(0,0)

        self.timer = 5
        self.kirbys = []
        self.index = 0

        for i in range(10):
            newKirby = Player((0,0), "kirby.png", (1,0))
            newKirby.animate = True
            self.kirbys.append(newKirby)


    def draw(self, drawSurface):
        drawSurface.fill((255,255,255))
        
        self.background.draw(drawSurface)
        self.waterLily.draw(drawSurface)
        self.rose.draw(drawSurface)
        self.carrot.draw(drawSurface)
        self.subRainbow.draw(drawSurface)
        
        self.kirby.draw(drawSurface)

        for k in self.kirbys:
            k.draw(drawSurface)
            
    def handleEvent(self, event):        
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = vec(*event.pos) // SCALE
            position += Drawable.CAMERA_OFFSET

            if self.rose.getCollisionRect().collidepoint(position):
                self.dragged = self.rose
                self.mouseOffset = self.rose.getPosition() - position
            #self.kirby.position = position
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragged = None
        elif event.type == pygame.MOUSEMOTION:
            position = vec(*event.pos) // SCALE
            position += Drawable.CAMERA_OFFSET
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

        for k in self.kirbys:
            k.update(seconds)

        self.timer -= seconds

        if self.timer <0:

            if self.index < len(self.kirbys):
                self.kirbys[self.index].position = vec(random.randint(0, RESOLUTION[0] - self.kirbys[self.index].getWidth()),
                       random.randint(0, RESOLUTION[1] - self.kirbys[self.index].getHeight()))
                self.index += 1
            self.timer = 5


        


        if self.kirby.getPosition()[0] <= 0:
            self.kirby.velocity[0] = 0
            self.kirby.position[0] = 0
        
        elif self.kirby.getPosition()[0] + self.kirby.getWidth() > WORLD_SIZE[0]:
            self.kirby.position[0] = WORLD_SIZE[0] - self.kirby.getWidth() 
            self.kirby.velocity[0]= 0
        
        if self.kirby.getPosition()[1] <= 0:
            self.kirby.velocity[1] = 0
            self.kirby.position[1] = 0
        elif self.kirby.getPosition()[1] + self.kirby.getHeight() > WORLD_SIZE[1]:
            self.kirby.position[1] = WORLD_SIZE[1] - self.kirby.getHeight()
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


        Drawable.CAMERA_OFFSET = self.kirby.getPosition() + self.kirby.getSize() /2 -  RESOLUTION //2 

        for i in range(2):
            Drawable.CAMERA_OFFSET[i] = max(min(Drawable.CAMERA_OFFSET[i], WORLD_SIZE[i] - RESOLUTION[i]), 
                                            0)