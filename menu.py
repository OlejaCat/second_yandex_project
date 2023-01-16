import pygame
import sys


pygame.init()
window = pygame.display.set_mode((1500, 800))


# стартовый экран
class Menu:
    def __init__(self, screen, points):
        self.screen = screen
        self.points = points

    def render(self, font, num_point):
        for i in self.points:
            if num_point == i[5]:
                window.blit(font.render(i[2], 3, i[4]), (i[0], i[1]))
            else:
                window.blit(font.render(i[2], 3, i[3]), (i[0], i[1]))

    def menu(self):
        running = True
        font_menu = pygame.font.Font(None, 80)

        point = 0
        while running:
            self.screen.fill(pygame.Color('black'))
            textures_1 = pygame.image.load('textures/labirint.jpg')
            window.blit(textures_1, (0, 0))
            mouse_pos = pygame.mouse.get_pos()
            for i in self.points:
                if (i[0] < mouse_pos[0] < i[0] + 100
                        and i[1] < mouse_pos[1] < i[1] + 100):
                    point = i[5]
                self.render(font_menu, point)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_UP:
                        if point > 0:
                            point -= 1
                    if event.key == pygame.K_DOWN:
                        if point < len(self.points) - 1:
                            point += 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if point == 0:
                        running = False
                    elif point == 1:
                        sys.exit()
            self.screen.blit(window, (0, 0))
            pygame.display.flip()
