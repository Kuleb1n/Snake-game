import sys
import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
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

    def is_game_grid(self):
        return 0 <= self.x < size_blocks and 0 <= self.y < size_blocks

    def __eq__(self, other):
        return isinstance(other, Snake) and self.x == other.x and self.y == other.y


def game_grid(color, row, column):
    pygame.draw.rect(screen, color, (size_blocks + size_blocks * column + MARGIN * (1 + column),
                                     header_margin + size_blocks + size_blocks * row + MARGIN * (1 + row),
                                     size_blocks, size_blocks))


def random_block_apple():
    random_x = random.randint(0, count_blocks - 1)
    random_y = random.randint(0, count_blocks - 1)
    empty_block = Snake(random_x, random_y)
    while empty_block in snake_body:
        empty_block.x = random.randint(0, count_blocks - 1)
        empty_block.y = random.randint(0, count_blocks - 1)
    return empty_block


snake_body = [Snake(9, 8), Snake(9, 9), Snake(9, 10)]
mov_column = 1
mov_row = 0
apple = random_block_apple()
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
    game_grid(RED, apple.x, apple.y)
    head = snake_body[-1]
    if not head.is_game_grid():
        pygame.quit()
        sys.exit()
    for block in snake_body:
        game_grid(GREEN, block.x, block.y)

    new_head = Snake(head.x + mov_row, head.y + mov_column)
    snake_body.append(new_head)
    snake_body.pop(0)
    if apple == new_head:
        apple = Snake(apple.x, apple.y)
        snake_body.append(apple)
        apple = random_block_apple()

    pygame.display.flip()
    time.tick(2)
