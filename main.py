import sys
import pygame
import random
import pygame_widgets
from pygame_widgets.button import Button

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
MARGIN = 1
header_margin = 70
count_blocks = 20
size_blocks = 20
screen = pygame.display.set_mode((size_blocks * count_blocks + MARGIN * count_blocks + 2 * count_blocks,
                                  size_blocks * count_blocks + MARGIN * count_blocks + header_margin + 2 * count_blocks))
pygame.display.set_caption('Snake')
pygame_icon = pygame.image.load('images/icon_game.jpg')
pygame.display.set_icon(pygame_icon)
font = pygame.font.SysFont('arial', 32)
time = pygame.time.Clock()


def my_menu():
    img_menu = pygame.image.load('images/photo_menu.jpg')

    def exit_game():
        pygame.quit()
        sys.exit()

    class Btn(Button):
        def __init__(self, win, x, y, width, height, **kwargs):
            super().__init__(win, x, y, width, height, **kwargs)

    btn_1 = Btn(screen, 300, 300, 150, 100,
                text='Play', font=pygame.font.SysFont('sans-serif', 46),
                margin=0, inactiveColour=(0, 255, 0), hoverColour=(0, 100, 0),
                radius=30,
                onClick=lambda: start_game()
                )
    btn_2 = Btn(screen, 300, 410, 150, 100,
                text='Exit', font=pygame.font.SysFont('sans-serif', 46),
                margin=0, inactiveColour=(255, 0, 0), hoverColour=(100, 0, 0), radius=30,
                onClick=lambda: exit_game())
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(img_menu, (0, 0))
        pygame_widgets.update(btn_1)
        pygame_widgets.update(btn_2)

        pygame.display.flip()


def start_game():
    class Snake:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def is_game_grid(self):
            return 0 <= self.x < count_blocks and 0 <= self.y < count_blocks

        def __eq__(self, other):
            return isinstance(other, Snake) and self.x == other.x and self.y == other.y

    def game_grid(color, row, column):
        pygame.draw.rect(screen, color,
                         (size_blocks + size_blocks * column + MARGIN * (1 + column),
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
    mov_column = const_colum = 1
    mov_row = const_row = 0
    score = 0
    speed = 1
    apple = random_block_apple()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and mov_column != 0:
                    const_row -= 1
                    const_colum = 0
                elif event.key == pygame.K_s and mov_column != 0:
                    const_row += 1
                    const_colum = 0
                elif event.key == pygame.K_a and mov_row != 0:
                    const_colum -= 1
                    const_row = 0
                elif event.key == pygame.K_d and mov_row != 0:
                    const_colum += 1
                    const_row = 0

        screen.fill(WHITE)
        pygame.draw.rect(screen, YELLOW,
                         (0, 0, size_blocks * count_blocks + MARGIN * count_blocks + 2 * count_blocks, 70))
        screen_text = font.render(f'Score: {score}', 0, (0, 0, 0))
        speed_text = font.render(f'Speed: {speed}', 0, (0, 0, 0))
        screen.blit(screen_text, (0, 0))
        screen.blit(speed_text, (250, 0))

        for row in range(count_blocks):
            for column in range(count_blocks):
                game_grid(BLACK, row, column)

        head = snake_body[-1]
        if not head.is_game_grid():
            my_menu()

        game_grid(RED, apple.x, apple.y)
        for block in snake_body:
            game_grid(GREEN, block.x, block.y)

        pygame.display.flip()
        if apple == head:
            score += 1
            speed = score // 5 + 1
            snake_body.append(apple)
            apple = random_block_apple()
        mov_column = const_colum
        mov_row = const_row
        new_head = Snake(head.x + mov_row, head.y + mov_column)

        if new_head in snake_body:
            my_menu()

        snake_body.append(new_head)
        snake_body.pop(0)
        time.tick(2 + speed)


my_menu()
