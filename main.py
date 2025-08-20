import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    # obj groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # setting group as containers for player obj
    Player.containers = (updatable, drawable)
    
    # player obj
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        
        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    
    
if __name__ == "__main__":
    main()
    