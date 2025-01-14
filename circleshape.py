import pygame # type: ignore

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.x = x
        self.y = y
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def check_collision(self, other_shape):
        distance = self.position.distance_to(other_shape.position)
        combined_radius = self.radius + other_shape.radius

        #print(f"Object 1: ({self.x}, {self.y})")
        #print(f"Object 2: ({other_shape.x}, {other_shape.y})")
        #print(f"Distance: {distance}")

        if distance <= combined_radius:
            return True
        return False