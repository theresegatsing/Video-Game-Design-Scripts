import pygame 
from vector import *
import time


def main():

    pygame.init()

    RESOLUTION = (800,400)  
    FACTOR = 2
    UPSCALED = [int(x* FACTOR) for x in RESOLUTION]
    screen = pygame.display.set_mode(list(UPSCALED))
    drawSurface = pygame.Surface(list(RESOLUTION))
    LuigiPos = vec(500,300)
    LuigiVel = vec(0,0)
    gameClock = pygame.time.Clock()

    RUNNING = True
    while RUNNING:
        screen.fill((255,255,255))
        drawSurface.fill((255,255,255))

        myFont = pygame.font.SysFont("Times New Roman", 14)
        Google = myFont.render("Google", False, (0,0,0))
        #screen.blit(Google, (400, 200))
        drawSurface.blit(Google, (400, 200))

        Luigi = pygame.image.load("C:/Users/gatsi/Box/winter 2026/video game design/Luigi.png").convert_alpha()
        #screen.blit(Luigi, (500, 300))
        drawSurface.blit(Luigi, pyVec(LuigiPos))

        pygame.transform.scale(drawSurface, list(UPSCALED), screen)



        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        LuigiVel[0] = 20
                    elif event.key == pygame.K_LEFT:
                        LuigiVel[0] = -20
                    elif event.key  == pygame.K_UP:
                        LuigiVel[1] = -20
                    elif event.key == pygame.K_DOWN:
                        LuigiVel[1] = 20


                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        LuigiVel[0] = 0
                    elif event.key == pygame.K_LEFT:
                        LuigiVel[0] = 0
                    elif event.key == pygame.K_UP:
                        LuigiVel[1] = 0
                    elif event.key == pygame.K_DOWN:
                        LuigiVel[1] = 0

        gameClock.tick()
        seconds = gameClock.get_time() / 1000.0
        LuigiPos += LuigiVel *seconds
    pygame.quit()



if __name__ == "__main__":
    main()