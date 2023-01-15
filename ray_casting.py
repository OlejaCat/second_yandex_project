import pygame

from settings import *
from load_map import level_map, MAP_WIDTH, MAP_HEIGHT


def corner_coords(a, b):
    return (a // TILE_SIZE) * TILE_SIZE, (b // TILE_SIZE) * TILE_SIZE


def ray_casting(player_pos, player_angle, textures):
    current_angle = player_angle - (FOV / 2)
    x0, y0 = player_pos
    cx, cy = corner_coords(x0, y0)
    horizontal_depth, vertical_depth = 0, 0
    horizontal_texture, vertical_texture = 1, 1
    distance_to_walls = []
    yv, xh = 0, 0

    for ray in range(NUMBER_OF_RAYS):
        sin = math.sin(current_angle)
        cos = math.cos(current_angle)

        x, dx = (cx + TILE_SIZE, 1) if cos >= 0 else (cx, -1)
        for i in range(0, MAP_WIDTH, TILE_SIZE):
            vertical_depth = (x - x0) / cos
            yv = y0 + vertical_depth * sin
            vertical_tile = corner_coords(x + dx, yv)
            if vertical_tile in level_map:
                vertical_texture = level_map[vertical_tile]
                break
            x += dx * TILE_SIZE

        y, dy = (cy + TILE_SIZE, 1) if sin >= 0 else (cy, -1)
        for i in range(0, MAP_HEIGHT, TILE_SIZE):
            horizontal_depth = (y - y0) / sin
            xh = x0 + horizontal_depth * cos
            horizontal_tile = corner_coords(xh, y + dy)
            if horizontal_tile in level_map:
                horizontal_texture = level_map[horizontal_tile]
                break
            y += dy * TILE_SIZE

        if vertical_depth < horizontal_depth:
            depth, offset, texture = (vertical_depth, yv, vertical_texture)
        else:
            depth, offset, texture = (horizontal_depth, xh, horizontal_texture)
        offset = int(offset) % TILE_SIZE
        depth *= math.cos(player_angle - current_angle)
        depth = max(depth, 0.00001)
        projection_height = min(int(PROJECTION_RATIO / depth), 2 * HEIGHT)
        distance_to_wall = (ray * SCALE, HALF_HEIGHT - projection_height // 2)
        part_of_wall = textures[texture].subsurface(offset * TEXTURE_SCALE, 0,
                                                    TEXTURE_SCALE, TEXTURE_HEIGHT)
        part_of_wall = pygame.transform.scale(part_of_wall, (SCALE, projection_height))
        distance_to_walls.append((depth, distance_to_wall, part_of_wall))

        current_angle += DELTA

    return distance_to_walls

