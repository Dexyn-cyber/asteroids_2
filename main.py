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
        for event in pygame.event.get(): # This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black") # This will fill the displays background
        player.draw(screen) # Draws the player on screen
        pygame.display.flip() # This will Update the contents of the entire display

        dt = clock.tick(60) / 1000 # update the clock [tick(framerate=0) -> milliseconds] will pause game loop every 1/60th of a second



if __name__ == "__main__":
    main()
