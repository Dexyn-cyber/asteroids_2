import pygame
from player_sub import Player
from shot_sub import Shot

from constants_sub import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TESTER FOR MAIN: NOT MAINGAME")
    clock = pygame.time.Clock()
    dt = 0 
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Manual Exit.")
                exit(1)

        updatable.update(dt)

        # Camera follows player
        camera_offset = pygame.Vector2(
            player.position.x - SCREEN_WIDTH // 2,
            player.position.y - SCREEN_HEIGHT // 2
        )

        screen.fill("black")  # clear screen

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()