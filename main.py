import sys

import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MARGIN = 1
header_margin = 70
count_blocks = 20
size_blocks = 20
screen = pygame.display.set_mode((size_blocks * count_blocks + MARGIN * count_blocks + 2 * count_blocks,
                                  size_blocks * count_blocks + MARGIN * count_blocks + header_margin + 2 * count_blocks))
pygame.display.set_caption('Snake')


def game_grid(row, column):
    pygame.draw.rect(screen, BLACK, (size_blocks + size_blocks * column + MARGIN * (1 + column),
                                     header_margin + size_blocks + size_blocks * row + MARGIN * (1 + row),
                                     size_blocks, size_blocks))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    for row in range(count_blocks):
        for column in range(count_blocks):
            game_grid(row, column)
    pygame.display.update()
