import pygame

from settings import *


# все что находится здесь направлено, на этображение миникарты
class MiniPlayer(pygame.sprite.Sprite):
    def __init__(self, radius, coins, check_point):
        super().__init__(all_mini_sprites)
        self.coins = coins
        self.check_point = check_point
        self.deleted = []
        self.deleted_coins = []
        self.coins_in_queue = 0
        self.coins_in_use = 0
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color('red'),
                           (radius, radius), radius)
        self.rect = self.image.get_rect()

    def update(self, x, y):
        self.rect.x = x // MAP_SCALE - 4
        self.rect.y = y // MAP_SCALE - 4
        coin = pygame.sprite.spritecollide(self, self.coins, False)
        if coin:
            temp = [coin for coin in self.coins]
            for element in self.deleted_coins:
                temp.insert(element[1], element[0])
            index = temp.index(coin[0])

            if index not in self.deleted:
                self.deleted.append(index)

            self.deleted_coins.append((coin[0], index))

            pygame.sprite.spritecollide(self, self.coins, True)
            self.coins_in_queue += 1
            return index

        if pygame.sprite.spritecollideany(self, self.check_point):
            self.coins_in_use += self.coins_in_queue
            self.coins_in_queue = 0

        return False


class MiniWalls(pygame.sprite.Sprite):
    def __init__(self, x, y, side):
        super().__init__(all_mini_sprites)
        self.add(mini_walls)
        self.image = pygame.Surface((side, side))
        pygame.draw.rect(self.image, pygame.Color('grey'),
                         (0, 0, side, side))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class MiniCoinMachine(pygame.sprite.Sprite):
    def __init__(self, x, y, side):
        super().__init__(all_mini_sprites)
        self.add(check_point)
        self.image = pygame.Surface((side, side))
        pygame.draw.rect(self.image, pygame.Color('green'),
                         (0, 0, side, side))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class MiniCoins(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(all_mini_sprites)
        self.add(mini_coins)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)

        pygame.draw.circle(self.image, pygame.Color('yellow'),
                           (radius, radius), radius)

        self.rect = self.image.get_rect()
        self.rect.x = x + 5
        self.rect.y = y + 5


all_mini_sprites = pygame.sprite.Group()
mini_walls = pygame.sprite.Group()
mini_coins = pygame.sprite.Group()
check_point = pygame.sprite.Group()


def mini_map(level_mini_map, coins_coords, check_point_coords):
    all_mini_sprites.empty()
    mini_walls.empty()
    mini_coins.empty()
    mini_map_x, mini_map_y = player_pos[0] // MAP_SCALE, player_pos[1] // MAP_SCALE
    for i, j in level_mini_map:
        MiniWalls(i, j, MINI_MAP_TILE_SIZE)
    for i, j in coins_coords:
        MiniCoins(i * MINI_MAP_TILE_SIZE, j * MINI_MAP_TILE_SIZE,
                  MINI_MAP_TILE_SIZE // 3)
    MiniCoinMachine(check_point_coords[0] * MINI_MAP_TILE_SIZE,
                    check_point_coords[0] * MINI_MAP_TILE_SIZE, MINI_MAP_TILE_SIZE)
    mini_player = MiniPlayer(RADIUS, mini_coins, check_point)

    return all_mini_sprites, mini_coins, mini_walls, mini_player, mini_map_x, mini_map_y
