import pygame
import os

from settings import *


def load_textures(name):
    fullname = os.path.join('textures', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        exit(0)
    image = pygame.image.load(fullname).convert()
    return image


# отображение части компонентов на экран
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
                self.screen.blit(wall[1], wall[2])

    def show_fps(self, clock):
        fps = str(int(clock.get_fps()))
        text = self.font.render(fps, False, pygame.Color('white'))
        self.screen.blit(text, FPS_POSITION)

    def show_collected(self, max_amount, current):
        text = self.font.render(f'{current}/{max_amount}', False, pygame.Color('white'))
        self.screen.blit(text, AMOUNT_POSITION)
