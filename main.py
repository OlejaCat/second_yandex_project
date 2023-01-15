import pygame

from settings import *
from player import Player
from ray_casting import ray_casting
from show_sprites import Sprites
from render import Render
from mini_map import all_mini_sprites
from level_system import define_level

pygame.init()
screen = pygame.display.set_mode(SIZE)
mini_map_screen = pygame.Surface((MINI_MAP_WIDTH, MINI_MAP_HEIGHT))
level = define_level()

clock = pygame.time.Clock()
sprites = Sprites(level['sprites'])
player = Player()
render = Render(screen, mini_map_screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    all_mini_sprites.update(player.x, player.y)
    player.motion()

    screen.fill(pygame.Color('black'))
    mini_map_screen.fill(pygame.Color('black'))

    render.draw_background()
    walls = ray_casting(player.pos, player.angle, render.textures)
    render.draw_level(walls + [obj.sprite_placement(player, walls)
                               for obj in sprites.all_sprites])
    render.show_fps(clock)

    all_mini_sprites.draw(mini_map_screen)
    screen.blit(mini_map_screen, MINI_MAP_POSITION)

    pygame.display.flip()
    clock.tick(FPS)
