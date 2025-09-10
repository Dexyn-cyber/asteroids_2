import random
import pygame
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        color_a = ''
        if self.radius >= (ASTEROID_MAX_RADIUS * 0.8): color_a = 'yellow'
        elif self.radius < (ASTEROID_MAX_RADIUS * 0.6) and self.radius > (ASTEROID_MAX_RADIUS * 0.4): color_a = "darkred"
        elif self.radius == ASTEROID_MIN_RADIUS: color_a = 'white'
        else: color_a = "blue"
        pygame.draw.circle(screen, color_a, self.position, self.radius, 10)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS: # BUG: creates phatoms if the = is not present as it ignore the 
            self.kill()
            return
        
        # Store values before any killing
        pos_x, pos_y = self.position.x, self.position.y
        vel = self.velocity.copy()
        radius = self.radius
        
        # Create new asteroids first
        angle = random.uniform(20, 50)
        a = vel.rotate(angle)
        b = vel.rotate(-angle)
        new_radius = radius - ASTEROID_MIN_RADIUS
        aster_a = Asteroid(pos_x, pos_y, new_radius)
        aster_b = Asteroid(pos_x, pos_y, new_radius)
        aster_a.velocity = a * 1.2
        aster_b.velocity = b * 1.2
        
        # Kill the original last
        self.kill()
