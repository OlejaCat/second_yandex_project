from settings import *


def load_level(file_name):
    with open(f'maps/{file_name}') as mapFile:
        mp = [line.strip().replace(' ', '.') for line in mapFile]

    max_width = max(map(len, mp))
    return list(map(lambda x: x.ljust(max_width, '.'), mp))


level_map = dict()
level_mini_map = set()
text_map = load_level(current_file_name)
coins_coords = set()
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
            coins_coords.add((i + 1, j + 1))



