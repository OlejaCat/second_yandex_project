import pygame
import os


from settings import *
from show_sprites import Sprite


def load_level(file_name):
    with open(f'maps/{file_name}') as mapFile:
        mp = [line.strip().replace(' ', '.') for line in mapFile]

    max_width = max(map(len, mp))
    return list(map(lambda x: x.ljust(max_width, '.'), mp))


def load_sprite(name):
    fullname = os.path.join('sprites', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        exit(0)
    image = pygame.image.load(fullname).convert_alpha()
    return image


# определние уровня
def define_level(level_number):
    sprite_types = {
        'coin': load_sprite('coin.png'),
        'slot_machine': load_sprite('slot_machine.png')
    }

    maps = ['map_1.txt', 'map_2.txt', 'map_3.txt']
    text_map = load_level(maps[level_number - 1])
    level_map = dict()
    level_mini_map = set()
    coins_coords = list()
    MAP_WIDTH, MAP_HEIGHT = len(text_map[0]) * TILE_SIZE, len(text_map) * TILE_SIZE
    for j, row in enumerate(text_map):
        for i, elem in enumerate(row):
            if elem not in ('.', 'c'):
                level_mini_map.add((i * MINI_MAP_TILE_SIZE, j * MINI_MAP_TILE_SIZE))
                if elem == '1':
                    level_map[(i * TILE_SIZE, j * TILE_SIZE)] = '1'
                if elem == '2':
                    level_map[(i * TILE_SIZE, j * TILE_SIZE)] = '2'
            if elem == 'c':
                coins_coords.append((i, j))

    levels_settings = {
        1: {
            'level_map': level_map,
            'level_mini_map': level_mini_map,
            'coins_coordinates': coins_coords,
            'MAP_SIZE': (MAP_WIDTH, MAP_HEIGHT),
            'check_point_coordinates': (6, 6),
            'sprites': ([Sprite(sprite_types['slot_machine'], 'coin_machine', (6.5, 6.5), 0.4, 0.75)]
                        + [Sprite(sprite_types['coin'], 'coin',
                                  (coin[0] + 0.5, coin[1] + 0.5), 0.3, 0.4) for coin in coins_coords]),
            'amount_of_coins': len(coins_coords)
        },
        2: {
            'level_map': level_map,
            'level_mini_map': level_mini_map,
            'coins_coordinates': coins_coords,
            'MAP_SIZE': (MAP_WIDTH, MAP_HEIGHT),
            'check_point_coordinates': (1, 1),
            'sprites': ([Sprite(sprite_types['slot_machine'], 'coin_machine', (1.5, 1.5), 0.4, 0.75)]
                        + [Sprite(sprite_types['coin'], 'coin',
                                  (coin[0] + 0.5, coin[1] + 0.5), 0.3, 0.4) for coin in coins_coords]),
            'amount_of_coins': len(coins_coords)
        },
        3: {
            'level_map': level_map,
            'level_mini_map': level_mini_map,
            'coins_coordinates': coins_coords,
            'MAP_SIZE': (MAP_WIDTH, MAP_HEIGHT),
            'check_point_coordinates': (1, 1),
            'sprites': ([Sprite(sprite_types['slot_machine'], 'coin_machine', (1.5, 1.5), 0.4, 0.75)]
                        + [Sprite(sprite_types['coin'], 'coin',
                                  (coin[0] + 0.5, coin[1] + 0.5), 0.3, 0.4) for coin in coins_coords]),
            'amount_of_coins': len(coins_coords)
        }
    }

    level = levels_settings[level_number]

    return level
