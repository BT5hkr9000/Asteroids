from circleshape import *
import pygame # type: ignore
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #self.x = x
        #self.y = y
        #self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, width=2)
    def update(self, dt):
        self.x += (self.velocity.x * dt)
        self.y += (self.velocity.y * dt)
        self.position.x = self.x
        self.position.y = self.y

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vector_one = pygame.math.Vector2.rotate(self.velocity, angle)
        vector_two = pygame.math.Vector2.rotate(self.velocity, -angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = vector_one * 1.2
        asteroid_two.velocity = vector_two * 1.2