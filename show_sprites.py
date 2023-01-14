import math

import pygame
import os

from settings import *


def load_sprite(name):
    fullname = os.path.join('sprites', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        exit(0)
    image = pygame.image.load(fullname).convert_alpha()
    return image


class Sprites:
    def __init__(self):
        self.types = {
            'slot_machine': load_sprite('slot_machine.png'),
            'coin': load_sprite('coin.png')
        }
        self.all_sprites = [
            Sprite(self.types['slot_machine'], False, (7.5, 4.5), 0.3, 0.75)
        ]


class Sprite:
    def __init__(self, type, static, pos, shift, scale):
        self.type = type
        self.static = static
        self.pos = self.x, self.y = pos[0] * TILE_SIZE, pos[1] * TILE_SIZE
        self.shift = shift
        self.scale = scale

        if not static:
            pass

    def sprite_placement(self, player, walls):
        dx, dy = self.x - player.x, self.y - player.y
        distance_to_sprite = math.sqrt((dx ** 2 + dy ** 2))
        walls = [walls[0]for _ in range(NUMBER_OF_FAKE_RAYS)] + walls + [walls[-1] for _ in range(NUMBER_OF_FAKE_RAYS)]
        betta = math.atan2(dy, dx)

        gamma = betta - player.angle
        if dx > 0 and 180 <= math.degrees(gamma) <= 360 or dx > 0 > dy:
            gamma += math.pi * 2

        delta_rays = int(gamma // DELTA)
        current_ray = CENTER_RAY + delta_rays
        distance_to_sprite = distance_to_sprite * math.cos((FOV // 2) - current_ray * DELTA)

        if (0 <= current_ray + NUMBER_OF_FAKE_RAYS + 2 <= NUMBER_OF_RAYS + 2 * NUMBER_OF_FAKE_RAYS
                and distance_to_sprite < walls[current_ray][0]):
            projection_height = min(int(PROJECTION_RATIO / distance_to_sprite * self.scale), HEIGHT * 2)
            shift = projection_height // 2 * self.shift

            sprite_pos = (current_ray * SCALE - projection_height // 2,
                          HALF_HEIGHT - projection_height // 2 + shift)
            sprite = pygame.transform.scale(self.type, (projection_height, projection_height))

            return distance_to_sprite, sprite_pos, sprite

        return False,
