import pygame

# Base class for game objects (circles)
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else: 
            super().__init__()
            
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        
    def draw(self, screen):
        # sub-classes must override
        pass
    
    def update(self, dt):
        # sub-classes must override
        pass
    
    def check_collisions(self, other_circle):
        distance = self.position.distance_to(other_circle.position)
        sum_radii = self.radius + other_circle.radius
        return distance <= sum_radii
