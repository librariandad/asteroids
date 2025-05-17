from constants import *
import pygame
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    containers = None


    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 180
        self.shot_timer = 0

    # in the player class
    def rotate(self, frame_rate):
        self.rotation += PLAYER_TURN_SPEED * frame_rate

    def move(self, frame_rate):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * frame_rate

    def shoot(self):
        # create a new shot
        if self.shot_timer <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.rotation = self.rotation
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            self.shot_timer = PLAYER_SHOT_COOLDOWN


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
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

        self.shot_timer -= dt
