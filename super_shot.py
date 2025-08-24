import pygame

from circleshape import CircleShape
from constants import SUPER_SHOT_RADIUS

class SuperShot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SUPER_SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt