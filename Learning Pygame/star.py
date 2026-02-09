import pygame
from vector import pyVec, vec
from drawable import Drawable
from mobile import Mobile, Player
RESOLUTION = vec(400,350)
SCALE = 2
UPSCALED = RESOLUTION * SCALE


class Star(object):

    def __init__(self):
        self.star =  Player((200,175), "star.png")
        self.background = Drawable((0,0), "background.png")


    def draw(self, screen):
        screen.fill((255,255,255))
        self.background.draw(screen)
        self.star.draw(screen)


    def handleEvent(self, event):

        self.star.handleEvent(event)

    def update(self, seconds):
        self.star.update(seconds)

        if self.star.getPosition()[0] <= 0:
            self.star.velocity[0] = - self.star.velocity[0] #Applies the bounce by reversing the velocity
            self.star.position[0] = 0
        
        elif self.star.getPosition()[0] + self.star.getWidth() > RESOLUTION[0]:
            self.star.position[0] = RESOLUTION[0] - self.star.getWidth() 
            self.star.velocity[0]= - self.star.velocity[0]
        
        if self.star.getPosition()[1] <= 0:
            self.star.velocity[1] = - self.star.velocity[1]
            self.star.position[1] = 0
        elif self.star.getPosition()[1] + self.star.getHeight() > RESOLUTION[1]:
            self.star.position[1] = RESOLUTION[1] - self.star.getHeight()
            self.star.velocity[1]= - self.star.velocity[1]

    def getCollisionRect(self):
        return self.star.getCollisionRect()
