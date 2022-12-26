# pygame 2.1.2; Python 3.10.2
'''Скрипт для рендера окна, игры Арканоид между двумя игроками,
с помощью одного устройства. Основанна данная программа на модуле
Pygame.
Краткая инструкция:
Кнопки:
R - перезауск игового процесса
W, S - перемщение вверх, вниз 1 платформы соответственно
UP, DOWN - перемщение вверх, вниз 2 платформы соответственно'''

import pygame
from random import choice, randint

# инициация всех зависимостей модуля
pygame.init()

# константы
HEIGHT = 500
WIDTH = HEIGHT * 2
PLATFORM_W, PLATRFORM_H = 20, 120 
RADIUS = 15
PLATFORM_SPEED = 15
BALL_SPEED_X, BALL_SPEED_Y = 5, 7

# внутримодульный пресчет времени
clock = pygame.time.Clock()

# название окна
pygame.display.set_caption('Arkanoid')
# создание основных поверхностей
screen = pygame.display.set_mode((WIDTH, HEIGHT))
surf1 = pygame.Surface((WIDTH, HEIGHT))

# шрифты
fonts = pygame.font.get_fonts()
font = pygame.font.SysFont('franklingothicheavy', 20)
font2 = pygame.font.SysFont('franklingothicheavy', 100, italic=True)
font3 = pygame.font.SysFont('franklingothicheavy', 50, italic=True)

# направление мяча
x_direction, y_direction = choice((-1 * BALL_SPEED_X, BALL_SPEED_X)), choice((-1 * BALL_SPEED_Y, BALL_SPEED_Y)) 

# скелеты для обработки коллизий и смещений объектов
ball_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, RADIUS * 2, RADIUS * 2)
platform1_rect = pygame.Rect(0, randint(0, HEIGHT - PLATRFORM_H), PLATFORM_W, PLATRFORM_H)
platform2_rect = pygame.Rect(WIDTH - PLATFORM_W, randint(0, HEIGHT - PLATRFORM_H), PLATFORM_W, PLATRFORM_H)

# переменные для работы с циклом
running, game_continue = True, True
# перемнные для определения параметров игры
score = 0
win = ''

while running:
    '''Основной цикл игры'''

    for event in pygame.event.get():
        '''Обработчик событий'''

        if event.type == pygame.QUIT:
            running = False
        
        # условие на рестарт игрового процесса
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                ball_rect.update(WIDTH // 2, HEIGHT // 2, RADIUS * 2, RADIUS * 2)
                score = 0
                game_continue = True

    # основные условия игры
    if game_continue:

        # блок отвечающий за перемещение платформ
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            if platform1_rect.y < HEIGHT - PLATRFORM_H:
                platform1_rect.move_ip(0, PLATFORM_SPEED)
        elif keys[pygame.K_w]:
            if platform1_rect.y > 0:
                platform1_rect.move_ip(0, -1 * (PLATFORM_SPEED))
        
        if keys[pygame.K_DOWN]:
            if platform2_rect.y < HEIGHT - PLATRFORM_H:
                platform2_rect.move_ip(0, PLATFORM_SPEED)
        elif keys[pygame.K_UP]:
            if platform2_rect.y > 0:
                platform2_rect.move_ip(0, -1 * (PLATFORM_SPEED))
        
        surf1.fill((0, 0, 0))

        # блок отвечающий за перемещение мяча и основные переменные игры
        if ball_rect.colliderect(platform1_rect) or ball_rect.colliderect(platform2_rect):
            x_direction *= -1
            score += 1
        if ball_rect.x <= 0 or ball_rect.x >= WIDTH:
            if ball_rect.x <= 0:
                win = 'RIGHT'
            else:
                win = 'LEFT'
            game_continue = False
        if ball_rect.y <= 0 or ball_rect.y >= HEIGHT:
            y_direction *= -1
        ball_rect.move_ip(x_direction, y_direction)

        # текст со счетом
        lable = f'SCORE {score}'
        lable_size = font.size(lable)
        score_surf = font.render(lable, False, (255, 255, 255))

        # отрисовка всех объектов
        pygame.draw.ellipse(surf1, (255, 255, 255), ball_rect)
        pygame.draw.rect(surf1, (255, 255, 255), platform1_rect)
        pygame.draw.rect(surf1, (255, 255, 255), platform2_rect)

        # размещение объектов
        surf1.blit(score_surf, (WIDTH // 2 - lable_size[0] // 2, 0))
        screen.blit(surf1, (0, 0))
    else:
        screen.fill((0, 0, 0))

        # текст 
        lable1, lable2 = f'{win} WIN', f'SCORE {score}'
        lable_size, lable_size2 = font2.size(lable1), font3.size(lable2) 
        end_surf = font2.render(lable1, False, (255, 255, 255)) 
        end_score_surf = font3.render(lable2, False, (255, 255, 255))

        # размещение текста
        screen.blit(end_surf, (WIDTH // 2 - lable_size[0] // 2, HEIGHT // 2 - lable_size[1] // 2))
        screen.blit(end_score_surf, (WIDTH // 2 - lable_size2[0] // 2, HEIGHT // 2 + 40))

        # полоски на весь экран
        for i in range(0, HEIGHT, 4):
            pygame.draw.line(screen, (0, 0, 0), (0, i), (1080, i), 2)

    # fps
    clock.tick(60)
    # обновление экрана
    pygame.display.update()

# точка выхода
pygame.quit()
