import pygame
from stats import player_stats 
import random

class Rogue_System():
    def __init__(self, x, y, width=600, height=50):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont("Arial", 24)

    # ON screen just need to implement it now on upgrade and keys

    def draw(self, screen):
        # Draws the background
        pygame.draw.rect(screen, "black", self.rect)
        pygame.draw.rect(screen, "blue", self.rect, 3)

        # render text | This will be side by side not down an up
        # Format = [(Upgrade) Cost=$[num]]
        option1 = self.font.render(f"Option 1 pick", True, 'gray')
        option2 = self.font.render(f"Option 2 pick", True, 'blue')
        option3 = self.font.render(f"Option 3 pick", True, 'red')

        screen.blit(option1, (self.rect.x + self.rect.width * 0.025, self.rect.y + 15))
        screen.blit(option2, (self.rect.x + self.rect.width * 0.35, self.rect.y + 15))
        screen.blit(option3, (self.rect.x + self.rect.width * 0.65, self.rect.y + 15))

    def buy_option(self, option):
        pass