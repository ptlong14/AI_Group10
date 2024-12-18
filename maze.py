import random
from node import Node


def generate_maze_dfs(grid, rows):
    def dfs(row, col):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        grid[row][col].reset()
        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc
            if 1 <= next_row < rows - 1 and 1 <= next_col < rows - 1:
                if grid[next_row][next_col].is_wall():
                    grid[row + dr // 2][col + dc // 2].reset()
                    dfs(next_row, next_col)

    for row in grid:
        for spot in row:
            spot.make_wall()
    dfs(1, 1)
