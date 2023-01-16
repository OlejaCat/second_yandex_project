import pygame

from settings import *
from player import Player
from ray_casting import ray_casting
from render import Render
from mini_map import mini_map
from load_level import define_level
from finish import Finish
from menu import Menu

pygame.init()
screen = pygame.display.set_mode(SIZE)
mini_map_screen = pygame.Surface((MINI_MAP_WIDTH, MINI_MAP_HEIGHT))
coin_amount = 0

game = Menu(screen, points)
game.menu()

# главный цикл программы, проход по всем уровням
for i in range(3):
    level = define_level(i + 1)
    mini = mini_map(level['level_mini_map'],
                    level['coins_coordinates'],
                    level[
                        'check_point_coordinates'])
    all_mini_sprites, mini_coins, mini_walls, mini_player, mini_map_x, mini_map_y = mini

    clock = pygame.time.Clock()
    all_sprites = level['sprites']
    player = Player(mini_player, mini_walls)
    render = Render(screen, mini_map_screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
        mini_player.update(player.x, player.y)
        if mini_player.coins_in_use == level['amount_of_coins']:
            coin_amount += mini_player.coins_in_use
            running = False
        player.motion()

        screen.fill(pygame.Color('black'))
        mini_map_screen.fill(pygame.Color('black'))

        render.draw_background()
        walls = ray_casting(player.pos, player.angle, render.textures,
                            level['level_map'], *level['MAP_SIZE'])

        sprites_with_coins = [sprite for sprite in all_sprites if sprite.type == 'coin']
        sprites_without_coins = [sprite for sprite in all_sprites if sprite.type != 'coin']

        true_coins = []
        for ind_coin in range(len(sprites_with_coins)):
            if ind_coin not in mini_player.deleted:
                true_coins.append(sprites_with_coins[ind_coin])

        sprites_without_coins.extend(true_coins)
        render.draw_level(walls + [obj.sprite_placement(player, walls)
                                   for obj in sprites_without_coins])
        render.show_fps(clock)
        render.show_collected(level['amount_of_coins'], mini_player.coins_in_use)

        all_mini_sprites.draw(mini_map_screen)
        screen.blit(mini_map_screen, MINI_MAP_POSITION)

        pygame.display.flip()
        clock.tick(FPS)

finish = Finish(screen, points, coin_amount)
finish.finish()