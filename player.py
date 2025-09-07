import pygame
import random

from constants import *
from circleshape import CircleShape
from shot import Shot
from stats import player_stats

from super_shot import SuperShot
from upgrades import upgrades_obj

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.super_shot_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Direction we're facing
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius        # TIP of triangle
        b = self.position - forward * self.radius - right  # Back-left corner
        c = self.position - forward * self.radius + right  # Back-right corner
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        self.shoot_timer -= dt
        self.super_shot_timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_x]:
            self.shoot_super()


    def move(self, dt):
        # Each frame, if W is pressed:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Direction player faces
        if upgrades_obj.speed == False:
            self.position += forward * PLAYER_SPEED * dt   # Move a tiny bit forward
        else:
            self.position += forward * UPGRADED_PLAYER_SPEED * dt 


    def shoot(self):
        if self.shoot_timer > 0:
            return
        if upgrades_obj.fire_rate == False:
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        else:
            self.shoot_timer = UPGRADED_PLAYER_SHOOT_COOLDOWN

        angle = random.uniform(-10, 10)
        
        if upgrades_obj.double_shot == True:
            for i in range(0, 2):
                shot = Shot(self.position.x , self.position.y)
                angle = random.uniform(-10, 10)
                shot.velocity = pygame.Vector2(0, 1).rotate((self.rotation + angle)) * PLAYER_SHOOT_SPEED
        else:
            shot = Shot(self.position.x , self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate((self.rotation + angle)) * PLAYER_SHOOT_SPEED
        player_stats.shot_bullet()

        

    def shoot_super(self):
        if self.super_shot_timer > 0:
            return
        for i in range(0, 11):
            angle = random.uniform(-25, 25)
            super_shot = SuperShot(self.position.x , self.position.y)
            super_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation + angle) * PLAYER_SHOOT_SPEED * 0.75 * 1.1
        self.super_shot_timer = PLAYER_SUPER_SHOT_COOLDOWN
