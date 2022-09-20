import sys

import pygame

pygame.init()

WHITE = (255, 255, 255)
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Snake')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    pygame.display.update()
