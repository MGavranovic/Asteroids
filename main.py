import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_WIDTH))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color=(000, 000, 000))

        pygame.display.flip()



if __name__ == "__main__":
    main()