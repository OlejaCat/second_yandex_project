import pygame
import sys


pygame.init()
window = pygame.display.set_mode((1200, 800))


# отрисовка конечного экрана
class Finish:
    def __init__(self, screen, points_2, coins_amount):
        self.screen = screen
        self.points = points_2
        self.coins_amount = coins_amount
        self.font = pygame.font.SysFont('Au diovide', 250, bold=True)
        self.font_2 = pygame.font.SysFont('Arial', 56, bold=True)

    def render(self, font, num_point):
        for i in self.points:
            if num_point == i[5]:
                window.blit(font.render(i[2], 3, i[4]), (i[0], i[1]))
            else:
                window.blit(font.render(i[2], 3, i[3]), (i[0], i[1]))

    def finish(self):
        running = True
        font_menu = pygame.font.Font(None, 80)

        point = 0
        while running:
            self.screen.fill(pygame.Color('black'))
            text = self.font.render('YOU WIN!!!', False, (161, 5, 5))
            text_2 = self.font_2.render(str(self.coins_amount), False, (0, 200, 200))
            textures_1 = pygame.image.load('textures/labirint_2.jpg')
            coin = pygame.image.load('sprites/coin_2.png')
            krest = pygame.image.load('sprites/krest.png')
            window.blit(textures_1, (0, 0))
            window.blit(text, (100, 100))
            window.blit(coin, (60, 430))
            window.blit(krest, (280, 490))
            window.blit(text_2, (380, 490))

            mouse_pos = pygame.mouse.get_pos()
            for i in self.points:
                if (i[0] < mouse_pos[0] < i[0] + 50
                        and i[1] < mouse_pos[1] < i[1] + 50):
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
