import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def did_we_collide(self, shape):
        if self.position.distance_to(shape.position) <= self.radius + shape.radius:
            return True
        return False

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass