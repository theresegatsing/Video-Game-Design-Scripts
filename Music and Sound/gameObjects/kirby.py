from . import Mobile
from FSMs import WalkingFSM, AccelerationFSM
from utils import vec, RESOLUTION
from gameObjects import Drawable

from pygame.locals import *

import pygame
import numpy as np


class Kirby(Mobile):
   def __init__(self, position):
      super().__init__(position, "kirby.png")

      self.hat = Drawable((0,0),"hat.png")
        
      # Animation variables specific to Kirby
      self.framesPerSecond = 2 
      self.nFrames = 2
      
      self.nFramesList = {
         "moving"   : 4,
         "standing" : 2
      }
      
      self.rowList = {
         "moving"   : 1,
         "standing" : 0
      }
      
      self.framesPerSecondList = {
         "moving"   : 8,
         "standing" : 2
      }
            
      self.FSManimated = WalkingFSM(self)
      self.LR = AccelerationFSM(self, axis=0)
      self.UD = AccelerationFSM(self, axis=1)
      
      
   def handleEvent(self, event):
      if event.type == KEYDOWN:
         if event.key == K_UP:
            self.UD.decrease()
             
         elif event.key == K_DOWN:
            self.UD.increase()
            
         elif event.key == K_LEFT:
            self.flipImage[0] = True
            self.LR.decrease()
            
         elif event.key == K_RIGHT:
            self.flipImage[0] = False
            self.LR.increase()
            
      elif event.type == KEYUP:
         if event.key == K_UP:
            self.UD.stop_decrease()
             
         elif event.key == K_DOWN:
            self.UD.stop_increase()
             
            
         elif event.key == K_LEFT:
            self.LR.stop_decrease()
            
         elif event.key == K_RIGHT:
            self.LR.stop_increase()

      
      elif event.type == JOYBUTTONDOWN:
         if event.button == 1:
            self.LR.increase()
      elif event.type == JOYBUTTONUP:
         if event.button == 1:
            self.LR.stop_increase()
      

      elif event.type == JOYHATMOTION:
         if event.hat == 0 :
            hatValue = event.value
            if hatValue[0] == 0:
               self.LR.stop_all()
            elif hatValue[0] == 1:
               self.LR.stop_all()

               self.LR.increase()

            elif hatValue[0] == -1:
               self.LR.stop_all()

               self.LR.decrease()

   
      elif event.type == JOYAXISMOTION:
         if event.axis == 0:
            if event.value < -0.5:
               self.LR.stop_all()

               self.LR.decrease()
            elif event.value > 0.5:
               self.LR.stop_all()

               self.LR.increase()
            else:
               self.LR.stop_all()
         
         elif event.axis == 1:
            if event.value < -0.5:
               self.UD.stop_all()
               self.UD.decrease()
            elif event.value > 0.5:
               self.UD.stop_all()
               self.UD.increase()
            else:
               self.UD.stop_all()


   def update(self, seconds): 
      self.LR.update(seconds)
      self.UD.update(seconds)
      self.hat.position = self.position
   
      super().update(seconds)
   
   
  