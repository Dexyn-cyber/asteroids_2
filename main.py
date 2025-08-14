import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from stats import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # create an object to help track time
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # This spawns play in the center of the screen

    while True:
    # 1. Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Goodbye.")
                return
        for aster in asteroids:
            if player.collides_with(aster):
                print("Game over!")
                print(player_stats.get_final_score())
                exit()

        for aster in asteroids:
            for shot in shots:
                if shot.collides_with(aster):
                    aster.split()
                    shot.kill()
                    player_stats.got_kill(aster)

        updatable.update(dt)

        screen.fill("black") # Draw screen first before objects, the objects get painted over.

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
