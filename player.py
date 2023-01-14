import pygame

from settings import *


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.pos = player_pos
        self.angle = player_angle

    def motion(self):
        sin = math.sin(self.angle)
        cos = math.cos(self.angle)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.x += player_speed * cos
            self.y += player_speed * sin
        if pressed[pygame.K_s]:
            self.x -= player_speed * cos
            self.y -= player_speed * sin
        if pressed[pygame.K_a]:
            self.x += player_speed * sin
            self.y -= player_speed * cos
        if pressed[pygame.K_d]:
            self.x -= player_speed * sin
            self.y += player_speed * cos
        if pressed[pygame.K_LEFT]:
            self.angle -= player_rotation_speed
        if pressed[pygame.K_RIGHT]:
            self.angle += player_rotation_speed
        self.pos = self.x, self.y
        self.angle = self.angle % (math.pi * 2)

    def get_pos(self):
        return self.x, self.y