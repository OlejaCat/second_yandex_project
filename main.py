import pygame

from settings import *
from player import Player
from ray_casting import ray_casting
from show_sprites import Sprites
from render import Render
from menu import Menu

pygame.init()
screen = pygame.display.set_mode(SIZE)
mini_map_screen = pygame.Surface((MINI_MAP_WIDTH, MINI_MAP_HEIGHT))

game = Menu(screen, points)
game.menu()

clock = pygame.time.Clock()
sprites = Sprites()
player = Player()
render = Render(screen, mini_map_screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    player.motion()
    screen.fill(pygame.Color('black'))

    render.draw_background()
    walls = ray_casting(player.pos, player.angle, render.textures)
    render.draw_level(walls + [obj.sprite_placement(player, walls)
                               for obj in sprites.all_sprites])
    render.draw_mini_map(player)
    render.show_fps(clock)

    pygame.display.flip()
    clock.tick(FPS)