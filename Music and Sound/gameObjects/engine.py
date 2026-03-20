import pygame
from utils import SoundManager

from . import Drawable, Kirby

from utils import vec, RESOLUTION

class GameEngine(object):
    import pygame

    def __init__(self):       
        self.kirby = Kirby((0,0))
        self.size = vec(*RESOLUTION)
        self.background = Drawable((0,0), "background.png")
    
    def draw(self, drawSurface):        
        self.background.draw(drawSurface)
        

        self.kirby.draw(drawSurface)
        self.kirby.hat.draw(drawSurface)
            
    def handleEvent(self, event):
        self.kirby.handleEvent(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            SoundManager.getInstance().playSFX("datacenter.flac")

    
    def update(self, seconds):
        self.kirby.update(seconds)
        
        Drawable.updateOffset(self.kirby, self.size)
    

