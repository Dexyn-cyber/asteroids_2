import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # create an object to help track time
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # This spawns play in the center of the screen


    while True:
    # 1. Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # 2. Update game state
        player.update(dt)

        # 3. Clear the screen
        #  (paint it black)
        screen.fill("dark red")
        
        # 4. Draw everything at their NEW positions
        player.draw(screen)
        
        # 5. Show the new frame to the user
        pygame.display.flip()

        # 6. Wait to maintain 60 FPS
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
