import pygame
from drawable import Drawable
from mobile import Mobile, Player
from os.path import join

class GameEngine(object):

    def __init__(self):        
        self.kirby = Player((0,0), "kirby.png", pygame.Rect(0,0,16,16), colorkey=True)
        self.background = Drawable((0,0), "background.png")
        self.waterLily = Drawable((250,100), "water-lily.png")
        self.rose = Drawable((100,100), "rose.png", pygame.Rect(4*34,0,34,62), transparency=True)
        self.carrot = Drawable((150,100), "plants.png", pygame.Rect(1,650,62,78), transparency=True)        
        self.subRainbow = Drawable((150,50), "rainbow.png", pygame.Rect(50,50,50,50))
        self.kirbySpeed = 100
    
    def draw(self, drawSurface):
        drawSurface.fill((255,255,255))
        
        self.background.draw(drawSurface)
        self.waterLily.draw(drawSurface)
        self.rose.draw(drawSurface)
        self.carrot.draw(drawSurface)
        self.subRainbow.draw(drawSurface)
        
        self.kirby.draw(drawSurface)
            
    def handleEvent(self, event):        
        self.kirby.handleEvent(event)        
    
    def update(self, seconds):
        self.kirby.update(seconds)

