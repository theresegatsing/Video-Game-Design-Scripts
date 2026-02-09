import pygame 
from vector import pyVec, vec
RESOLUTION = vec(400,350)
SCALE = 2
UPSCALED = RESOLUTION * SCALE
from star import Star
from orbs import Orbs


def main():
    #Initialize the module
    pygame.init()
        
    pygame.font.init()
        
        
    #Get the screen
    screen = pygame.display.set_mode(pyVec(UPSCALED))
    drawSurface = pygame.Surface(pyVec(RESOLUTION))
    gameClock = pygame.time.Clock()

    star = Star()
    orb = Orbs()
    
    RUNNING = True
        
    while RUNNING:
            
        pygame.transform.scale(drawSurface,
                                pyVec(UPSCALED),
                                screen)
        
        pygame.display.flip()
            
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                # change the value to False, to exit the main loop
                RUNNING = False
            
            else:
                star.handleEvent(event)
                orb.handleEvent(event)

        #Update 
        gameClock.tick(60)
        seconds = gameClock.get_time() / 1000
        star.update(seconds)
        orb.update(seconds, star)
        


        #Draw 
        star.draw(drawSurface)
        orb.draw(drawSurface)

       

    pygame.quit()


if __name__ == '__main__':
    main()