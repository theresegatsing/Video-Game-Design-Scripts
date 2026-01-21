import pygame 
from vector import *

class Drawable(object):

    def __init__(self, position, image):
        self.position = position
        self.image = image
    
    def draw(self, surface):
        surface.blit(self.image, pyVec(self.position))
    
    def getPosition(self):
        return self.position
    
    def setPosition(self, Pos):
        self.position = Pos
    
    def update(self, seconds):
        pass
    
    def handleEvent(self, event):
        pass

class Mobile(Drawable):
    def __init__(self, position, image):
        super().__init__(position, image)
        self.velocity = vec(0,0)
    
    def update(self, seconds):
        self.position += self.velocity * seconds

