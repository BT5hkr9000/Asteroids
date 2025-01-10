# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import * # type: ignore

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") # type: ignore
    print(f"Screen height: {SCREEN_HEIGHT}") # type: ignore

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000)
        pygame.display.flip()

if __name__ == "__main__":
    main()