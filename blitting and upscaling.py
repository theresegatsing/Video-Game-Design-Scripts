import pygame 

def main():

    pygame.init()

    RESOLUTION = (800,400)  
    FACTOR = 2
    UPSCALED = [int(x* FACTOR) for x in RESOLUTION]
    screen = pygame.display.set_mode(list(UPSCALED))
    drawSurface = pygame.Surface(list(RESOLUTION))

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
        drawSurface.blit(Luigi, (500, 300))

        pygame.transform.scale(drawSurface, list(UPSCALED), screen)



        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
    
    pygame.quit()



if __name__ == "__main__":
    main()