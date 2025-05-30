# import pygame
# import time
from circleshape import *
from constants import *
from shot import *


class Player(CircleShape):


    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0
        self.shot_timer = 0

    # note self.position is an attribute in the parent class CircleShape

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt


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
            self.shoot(dt)


    def move(self, dt):

        """ 
        We start with a unit vector pointing straight up from (0, 0) to (0, 1).
            We rotate that vector by the player's rotation, so it's pointing in the direction the player is facing.
            We multiply by PLAYER_SPEED * dt. A larger vector means faster movement.
            Add the vector to our position to move the player.

        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def shoot(self,dt):
        if self.shot_timer < 0:
            new_shot = Shot(self.position, self.position, SHOT_RADIUS)
            new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_timer = PLAYER_SHOOT_COOLDOWN

        self.shot_timer -= dt

