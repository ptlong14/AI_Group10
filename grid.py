import pygame
from node import Node
from settings import GRID
pygame.init()

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Node(i, j, gap, rows)
            grid[i].append(spot)
    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GRID, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GRID, (i * gap, 0), (i * gap, width))


def draw_grid_wall(rows, grid):
    pass


def draw(win, grid, rows, width):
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    draw_grid_wall(rows, grid)
    pygame.display.update()
