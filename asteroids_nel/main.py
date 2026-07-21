import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid 
from asteroidfield import AsteroidField 


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # pygame.Surface
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #Player1 = Player(0,1)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField1 = AsteroidField()
    Player1 = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_clock = pygame.time.Clock() # pygame.Clock
    dt = 0.0
    while True:
        log_state()
        dt = game_clock.tick(60) / 1000
        #print(dt) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black") # pygame.Rect
        for shape in drawable:
            shape.draw(screen)
        updatable.update(dt)
        pygame.display.flip() # None:


if __name__ == "__main__":
    main()
