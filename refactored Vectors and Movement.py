import pygame 
from vector import *
import time
from gameEngine import GameEngine
from drawable import Drawable



def main():

    pygame.init()

    RESOLUTION = (800,400)  
    FACTOR = 2
    UPSCALED = [int(x* FACTOR) for x in RESOLUTION]

    screen = pygame.display.set_mode(list(UPSCALED))
    drawSurface = pygame.Surface(list(RESOLUTION))
    

    gameClock = pygame.time.Clock()

    game = GameEngine()
    
    RUNNING = True
    while RUNNING:
        
        game.draw(drawSurface)

        pygame.transform.scale(drawSurface, list(UPSCALED), screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            
            else:
                game.handleEvent(event)

        gameClock.tick()
        seconds = gameClock.get_time() / 1000.0
        game.update(seconds)
    pygame.quit()



if __name__ == "__main__":
    main()