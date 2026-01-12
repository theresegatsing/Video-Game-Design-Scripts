import pygame 

def main():

    pygame.init()

    screen = pygame.display.set_mode((800,400))

    RUNNING = True
    while RUNNING:
        screen.fill((255,255,255))

        pygame.draw.circle(screen, (0,0,255), (400,200), 50)
        pygame.draw.rect(screen, (157, 23, 54), (180, 179, 23,89))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
    
    pygame.quit()



if __name__ == "__main__":
    main()