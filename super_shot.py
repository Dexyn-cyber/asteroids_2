import pygame

from circleshape import CircleShape
from constants import SUPER_SHOT_RADIUS

class SuperShot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SUPER_SHOT_RADIUS)

    def draw(self, screen):
        xy = SUPER_SHOT_RADIUS
        pygame.draw.rect(screen, "yellow", (xy,xy,xy,xy))

    def update(self, dt):
<<<<<<< HEAD
        self.velocity += 200 * dt FIX THIS
=======
        self.position += self.velocity * dt
>>>>>>> origin/super_shot
