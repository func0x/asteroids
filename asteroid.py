import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        angle = random.uniform(20, 50)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a_1 = Asteroid(self.x, self.y, new_radius)
        a_2 = Asteroid(self.x, self.y, new_radius)
        a_1.velocity = self.velocity.rotate(angle)
        a_1.velocity.scale_to_length(1.2)
        a_2.velocity = self.velocity.rotate(-angle)
        a_2.velocity.scale_to_length(1.2)