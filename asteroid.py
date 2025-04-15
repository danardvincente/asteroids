import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_split_asteroid_angle = random.uniform(20, 50)
            asteroid_veloc_1 = self.velocity.rotate(new_split_asteroid_angle)
            asteroid_veloc_2 = self.velocity.rotate(-new_split_asteroid_angle)

            sm_new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid_1 = Asteroid(self.position, self.position, sm_new_radius)
            new_asteroid_1.velocity = asteroid_veloc_1 * 1.2

            new_asteroid_2 = Asteroid(self.position, self.position, sm_new_radius)
            new_asteroid_2.velocity = asteroid_veloc_2