import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        vector_one = self.velocity.rotate(random_angle)
        vector_two = self.velocity.rotate(-(random_angle))
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_roid_one = Asteroid(self.position[0],self.position[1],new_radius)
        new_roid_two = Asteroid(self.position[0],self.position[1],new_radius)
        new_roid_one.velocity = vector_one * 1.2
        new_roid_two.velocity = vector_two * 1.2



    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position +=  self.velocity * dt