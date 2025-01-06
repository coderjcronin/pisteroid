# this allows us to use code from
# the open-source pygame library
# throught this file
import pygame
from constants import *

def main ():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frames_clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()
        dt = (frames_clock.tick(60)/1000)

if __name__ == "__main__":
    main()
