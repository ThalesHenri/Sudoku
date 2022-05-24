import pygame
import requests

# pygame init and vars
pygame.init()
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
original_grid = [[grid[x][y]for y in range(len(grid[0]))] for x in range(len(grid))]

# Colors
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0
WHITE = 255, 255, 255
LIGHT_BLUE = 100, 100, 255
BACK_GROUND_COLOR = 251, 247, 245

# Screen config
HEIGTH = 600
WIDTH = 900

# gameloop
def draw_grid(win):
    lines = 10 
    line_thickness = 2
    inside_line_thickness = 4

    for i in range(0, lines):
        if i%3 == 0:
            pygame.draw.line(win, (BLACK), (50 + 50 * i, 50), (50 + 50 * i, 500), inside_line_thickness)
            pygame.draw.line(win, (BLACK), (50, 50 * i + 50), (500, 50 + 50 * i), inside_line_thickness)
        pygame.draw.line(win, (BLACK), (50 + 50 * i, 50), (50 + 50 * i, 500), line_thickness)
        pygame.draw.line(win, (BLACK), (50, 50 * i + 50), (500, 50 + 50 * i), line_thickness)
        pygame.display.update()

def main():
    SCREEN = pygame.display.set_mode((WIDTH, HEIGTH))
    pygame.display.set_caption('Sudoku')
    SCREEN.fill((LIGHT_BLUE))
    pygame.display.update()
    font = pygame.font.SysFont('Courier New', 35, bold=True)
    run = True

    # entering values on the grid
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0 < grid[i][j] < 10):
                value = font.render(str(grid[i][j]), True, BLACK)
                # putting the values on the screen
                SCREEN.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50 + 10))
                # the '15' and the '10' is the element position in the grid



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

