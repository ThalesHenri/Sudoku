import pygame
import pandas as pd
import math
import random

# Colors
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0
WHITE = 255, 255, 255
LIGHT_BLUE = 100, 100, 255

# Screen config
HEIGTH = 1000
WIDTH = 700
SCREEN = pygame.display.set_mode((HEIGTH, WIDTH))

# Game config and vars
pygame.init()
font = pygame.font.SysFont('Courier New', 50, bold=True)
run = True

# Game loop
while run:
    for event in pygame.event.get():  # event catcher. New way of doing this with pygame.quit
        if event.type == pygame.QUIT:
            pygame.quit()
    