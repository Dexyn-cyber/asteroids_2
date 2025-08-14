from constants import *
import pygame

def main():
    print("Starting Asteroids! \n"
    f"Screen width: {SCREEN_WIDTH}\n"
    f"Screen height: {SCREEN_HEIGHT}")


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill("black") # This will open up the display
    while True:
        pygame.display.flip() # This will Update the contents of the entire display
        
        for event in pygame.event.get(): # This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
            if event.type == pygame.QUIT:
                return



    


if __name__ == "__main__":
    main()
