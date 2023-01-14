"""pygame.draw.circle(screen, pygame.Color('red'), (int(player.x), int(player.y)), 12)
    pygame.draw.line(screen, pygame.Color('red'), player.pos,
                     (player.x + WIDTH * math.cos(player.angle),
                      player.y + WIDTH * math.sin(player.angle)))

    for x, y in world_map:
        pygame.draw.rect(screen, pygame.Color('grey'),
                         (x, y, TILE_SIZE, TILE_SIZE), 2)"""


# old ray casting
"""

def ray_casting(screen, player_pos, player_angle):
    current_angle = player_angle - (FOV // 2)
    x0, y0 = player_pos

    for ray in range(NUMBER_OF_RAYS):
        sin = math.sin(current_angle)
        cos = math.cos(current_angle)
        for depth in range(DEPTH):
            x = x0 + depth * cos
            y = y0 + depth * sin
            if (x // TILE_SIZE * TILE_SIZE, y // TILE_SIZE * TILE_SIZE) in world_map:
                depth *= math.cos(player_angle - current_angle)
                r = 255 / (1 + depth * depth * 0.000005)
                color = (r, r // 2, r // 3)
                projection_height = PROJECTION_RATIO / depth
                pygame.draw.rect(screen, color,
                                 (ray * SCALE, HEIGHT // 2 - projection_height // 2,
                                  SCALE, projection_height))
                break

        current_angle += DELTA"""


"""r = 255 / (1 + depth**2 * 0.000003)
        color = (r // 2, r, r // 3)
        pygame.draw.rect(screen, color,
                         (ray * SCALE, HEIGHT // 2 - projection_height // 2,
                          SCALE, projection_height))"""



import PIL


























