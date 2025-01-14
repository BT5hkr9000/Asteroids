# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import * # type: ignore
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") # type: ignore
    print(f"Screen height: {SCREEN_HEIGHT}") # type: ignore

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    clock = pygame.time.Clock()
    dt = 0

    asteroid_field = AsteroidField()

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60)/1000
        for object in updatable:
            object.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()
        for object in drawable:
            object.draw(screen)
#        player.update(dt)
#        player.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()