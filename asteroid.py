import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    containers = None
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def rotate(self, frame_rate):
        pass

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            child_angle = random.uniform(20,50)
            child_radius = self.radius - ASTEROID_MIN_RADIUS
            child1 = Asteroid(self.position.x, self.position.y, child_radius)
            child2 = Asteroid(self.position.x, self.position.y, child_radius)
            child1.velocity = self.velocity.rotate(child_angle) * 1.2
            child2.velocity = self.velocity.rotate(-child_angle) * 1.2
        self.kill()




    def move(self, frame_rate):
        self.position += self.velocity * frame_rate

    def update(self, dt):
        self.move(dt)