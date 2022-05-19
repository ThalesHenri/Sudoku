import pygame
import pandas as pd
import math
import random

  # initialization of pygame
pygame.init()

# Colors
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0
WHITE = 255, 255, 255
LIGHT_BLUE = 100, 100, 255
BACK_GROUND_COLOR = 251,247,245

# Screen config
HEIGTH = 600
WIDTH = 900

# gameloop
def draw_grid(win):
    lines = 10
    for i in range(0, lines):
        pygame.draw.line(win, (BLACK),(50 + 50 * i, 50), (50 + 50*i, 500), 2)
        pygame.draw.line(win, (BLACK),(50, 50 * i + 50), (500, 50 + 50*i), 2)
        pygame.display.update()

def main():
    SCREEN = pygame.display.set_mode((WIDTH, HEIGTH))
    pygame.display.set_caption('Sudoku')
    SCREEN.fill((LIGHT_BLUE))
    pygame.display.update()
    font = pygame.font.SysFont('Courier New', 50, bold=True)
    run = True
    while run:
        # event catcher. New way of doing this with pygame.quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                exit()
            if event.type == pygame.KEYDOWN:  # will get the key pressed
                key_pressed = pygame.key.name(event.key)
                print(key_pressed)
        draw_grid(SCREEN)


main()

