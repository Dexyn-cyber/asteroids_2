import pygame

from circleshape import CircleShape
from constants import SUPER_SHOT_RADIUS

class SuperShot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SUPER_SHOT_RADIUS)
        self.velocity = 200

    def draw(self, screen):
        xy = SUPER_SHOT_RADIUS
        pygame.draw.rect(screen, "yellow", (xy,xy,xy,xy))

    def update(self, dt):
        self.position.y += 200 * dt