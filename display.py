import pygame
HEIGHT,WIDTH = 800,500
WDOW = pygame.display.set_mode((WIDTH,HEIGHT,))
pygame.display.set_caption('Hola')

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                break
    pygame.quit()


main()





