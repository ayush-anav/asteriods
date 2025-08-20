import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    # obj groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # setting group as containers for player obj
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots)
    # player obj
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        
        # check collisions if r1 + r2 <= circle1.raidus + circle2.radius
        for asteriod in asteroids:
            if(asteriod.check_collisions(player)):
                print("Game over!")
                sys.exit()
                
       
                
        # for shots
        shots.update(dt)
        for shot in shots:
            shot.draw(screen)
            
        for draw in drawable:
            draw.draw(screen)


        # check collisions if r1 + r2 <= circle1.raidus + circle2.radius
        for asteriod_bullet in asteroids:
            for shot in shots:
                if(asteriod_bullet.check_collisions(shot)):
                    asteriod_bullet.split()
                    shot.kill()
                
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    
    
if __name__ == "__main__":
    main()
    