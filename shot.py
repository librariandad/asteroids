import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    containers = None
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def rotate(self, frame_rate):
        pass

    def move(self, frame_rate):
        self.position += self.velocity * frame_rate

    def update(self, dt):
        self.move(dt)