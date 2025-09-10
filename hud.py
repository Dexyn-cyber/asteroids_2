import pygame
from stats import player_stats

class HUD:
    def __init__(self, x, y, width=150, height=100):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont(None, 24)

    def draw(self, screen):
        #Draw background box
        pygame.draw.rect(screen, (30, 30, 30), self.rect) # dark grey background [background fill]
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2) # white border [border only]

        # render text
        kills_text = self.font.render(f"Kills: {player_stats.kills}", True, (255, 255, 255))
        score_text = self.font.render(f"Score: {player_stats.score}", True, (255, 255, 255))
        health_text = self.font.render(f"Health: {player_stats.health}", True, (255, 255, 255))

        # Blit text into the box with padding(Postion's the text)
        screen.blit(kills_text, (self.rect.x + 10, self.rect.y + 10))
        screen.blit(score_text, (self.rect.x + 10, self.rect.y + 40))
        screen.blit(health_text, (self.rect.x + 10, self.rect.y + 70))
