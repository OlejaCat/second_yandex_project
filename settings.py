import math


# screen settings
SIZE = WIDTH, HEIGHT = 1500, 800
HALF_WIDTH, HALF_HEIGHT = WIDTH // 2, HEIGHT // 2
FPS = 60
FPS_POSITION = (WIDTH - 50, 0)

# player settings
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 3
player_rotation_speed = 0.04

# map settings
current_file_name = 'map.txt'
TILE_SIZE = 100

# mini map settings
MINIMAP_SCALE = 5
MINI_MAP_WIDTH = WIDTH // MINIMAP_SCALE
MINI_MAP_HEIGHT = HEIGHT // MINIMAP_SCALE
MAP_SCALE = 2 * MINIMAP_SCALE
MINI_MAP_TILE_SIZE = TILE_SIZE // MAP_SCALE
MINI_MAP_POSITION = (0, HEIGHT - HEIGHT // MAP_SCALE)

# texture settings
TEXTURE_WIDTH, TEXTURE_HEIGHT = 1500, 1500
TEXTURE_SCALE = TEXTURE_WIDTH // TILE_SIZE

# ray casting settings
FOV = math.pi / 3
NUMBER_OF_RAYS = 300
NUMBER_OF_FAKE_RAYS = 100
DEPTH = 1000
DELTA = FOV / NUMBER_OF_RAYS
DISTANCE = NUMBER_OF_RAYS / (2 * math.tan(FOV / 2))
PROJECTION_RATIO = 4 * DISTANCE * TILE_SIZE
SCALE = WIDTH // NUMBER_OF_RAYS


# sprite settings
CENTER_RAY = NUMBER_OF_RAYS // 2

# colors
SKY_COLOR = (0, 180, 255)
FLOOR_COLOR = (40, 40, 40)

# menu settings
points = [(650, 200, 'Play', (250, 250, 250), (161, 5, 5), 0),
          (650, 400, 'Exit', (250, 250, 250), (161, 5, 5), 1)]