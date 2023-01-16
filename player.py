import pygame

from settings import *
from mini_map import mini_walls


# игрок, в нем управление, проверка коллизий
class Player:
    def __init__(self, mini_player, mini_walls):
        self.x, self.y = player_pos
        self.pos = player_pos
        self.angle = player_angle
        self.mini_player = mini_player
        self.mini_walls = mini_walls
        self.picked_up_coins = 0

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
        self.mini_player.update(ox + player_speed, oy + player_speed)
        if not pygame.sprite.spritecollideany(self.mini_player, mini_walls):
            self.pos = ox, oy
            self.x, self.y = self.pos
        self.angle = self.angle % (math.pi * 2)
        self.mini_player.update(ox + player_speed, oy + player_speed)
        if not pygame.sprite.spritecollideany(self.mini_player, self.mini_walls):
            self.pos = ox, oy
            self.x, self.y = self.pos
        self.angle %= (math.pi * 2)
