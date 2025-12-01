import pygame

from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS
from logger import log_state
from player import Player
from asteroid import Asteroid
from logger import log_event
from shot import Shot
import sys


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    running = True
    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        log_state()

        updatable.update(dt)


        screen.fill("black")
        for u in updatable:
            u.update(dt)

        for d in drawable:
            d.draw(screen)

        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for s in shots:
                if a.collides_with(s):
                    log_event("asteroid_shot")
                    a.split()
                    s.kill()

        pygame.display.flip()


if __name__ == "__main__":
    main()
