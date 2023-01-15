import pygame

from settings import *
from mini_map import mini_player, mini_walls


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.pos = player_pos
        self.angle = player_angle

    def motion(self):
        sin = math.sin(self.angle)
        cos = math.cos(self.angle)
        ox, oy = self.pos
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            ox = self.x + player_speed * cos
            oy = self.y + player_speed * sin
        if pressed[pygame.K_s]:
            ox = self.x - player_speed * cos
            oy = self.y - player_speed * sin
        if pressed[pygame.K_a]:
            ox = self.x + player_speed * sin
            oy = self.y - player_speed * cos
        if pressed[pygame.K_d]:
            ox = self.x - player_speed * sin
            oy = self.y + player_speed * cos
        if pressed[pygame.K_LEFT]:
            self.angle -= player_rotation_speed
        if pressed[pygame.K_RIGHT]:
            self.angle += player_rotation_speed
        mini_player.update(ox + player_speed, oy + player_speed)
        if not pygame.sprite.spritecollideany(mini_player, mini_walls):
            self.pos = ox, oy
            self.x, self.y = self.pos
        self.angle = self.angle % (math.pi * 2)
