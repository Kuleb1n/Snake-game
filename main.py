import sys

import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
MARGIN = 1
header_margin = 70
count_blocks = 20
size_blocks = 20
screen = pygame.display.set_mode((size_blocks * count_blocks + MARGIN * count_blocks + 2 * count_blocks,
                                  size_blocks * count_blocks + MARGIN * count_blocks + header_margin + 2 * count_blocks))
pygame.display.set_caption('Snake')
time = pygame.time.Clock()


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def game_grid(color, row, column):
    pygame.draw.rect(screen, color, (size_blocks + size_blocks * column + MARGIN * (1 + column),
                                     header_margin + size_blocks + size_blocks * row + MARGIN * (1 + row),
                                     size_blocks, size_blocks))


snake_body = [Snake(9, 8), Snake(9, 9), Snake(9, 10)]
mov_column = 1
mov_row = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and mov_column != 0:
                mov_row -= 1
                mov_column = 0
            elif event.key == pygame.K_s and mov_column != 0:
                mov_row += 1
                mov_column = 0
            elif event.key == pygame.K_a and mov_row != 0:
                mov_column -= 1
                mov_row = 0
            elif event.key == pygame.K_d and mov_row != 0:
                mov_column += 1
                mov_row = 0

    screen.fill(WHITE)
    for row in range(count_blocks):
        for column in range(count_blocks):
            game_grid(BLACK, row, column)
    for block in snake_body:
        game_grid(GREEN, block.x, block.y)
        block.x += mov_row
        block.y += mov_column
    pygame.display.flip()
    time.tick(2)
