import pygame
import os

from settings import *
from load_map import level_mini_map


def load_textures(name):
    fullname = os.path.join('textures', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        exit(0)
    image = pygame.image.load(fullname).convert()
    return image


class Wall(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__()


class Star(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__()


class MiniPlayer(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__()


class Render:
    def __init__(self, screen, mini_map_screen):
        self.screen = screen
        self.mini_map_screen = mini_map_screen
        self.font = pygame.font.SysFont('Arial', 26, bold=True)
        self.textures = {'1': load_textures('walls/img.png'),
                         '2': load_textures('walls/img_1.png')}

    def draw_background(self):
        pygame.draw.rect(self.screen, SKY_COLOR, (0, 0, WIDTH, HEIGHT // 2))
        pygame.draw.rect(self.screen, FLOOR_COLOR, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    def draw_level(self, objects):
        for wall in sorted(objects, key=lambda x: x[0], reverse=True):
            if wall[0]:
                self.screen.blit(wall[2], wall[1])

    def draw_mini_map(self, player):
        self.mini_map_screen.fill(pygame.Color('black'))
        mini_map_x, mini_map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(self.mini_map_screen, pygame.Color('red'),
                         (mini_map_x, mini_map_y),
                         (mini_map_x + 15 * math.cos(player.angle),
                          mini_map_y + 15 * math.sin(player.angle)))
        pygame.draw.circle(self.mini_map_screen, pygame.Color('red'), (mini_map_x, mini_map_y), 6)

        for x, y in level_mini_map:
            pygame.draw.rect(self.mini_map_screen, pygame.Color('grey'),
                             (x, y, MINI_MAP_TILE_SIZE, MINI_MAP_TILE_SIZE))
        self.screen.blit(self.mini_map_screen, MINI_MAP_POSITION)

    def show_fps(self, clock):
        fps = str(int(clock.get_fps()))
        text = self.font.render(fps, False, pygame.Color('white'))
        self.screen.blit(text, FPS_POSITION)
