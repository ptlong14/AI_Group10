import pygame
from timeit import default_timer as timer
from grid import make_grid, draw
from maze import generate_maze_dfs
from algorithm import algorithm, reconstruct_path
from ui import draw_button, get_mouse_pos, draw_multiline_text, draw_instruction_box, draw_result_box
from message import display_message
from instructions import get_instructions
from settings import FONT

pygame.init()
MAZE_WIDTH = 665
WINDOW_WIDTH = 1000
HEIGHT = 665
win = pygame.display.set_mode((WINDOW_WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver ( Using A* Algorithm )")
ROWS = 35


def show_instructions():
    instructions = get_instructions()
    draw_instruction_box(win, instructions)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                waiting = False
            if event.type == pygame.KEYDOWN:
                waiting = False

def main():
    grid = make_grid(ROWS, MAZE_WIDTH)
    Start = None
    End = None
    Run = True
    result_message = "Result:\n" + "No result yet"

    def start_algorithm():
        nonlocal Start, End, result_message
        if not Start and not End:
            display_message(
                win, "Please select both Start and End points!", FONT)
            return
        elif not Start:
            display_message(win, "Please select a Start point!", FONT)
            return
        elif not End:
            display_message(win, "Please select an End point!", FONT)
            return
        if Start and End:
            counter_start = timer()
            pygame.display.set_caption("Maze Solver ( Searching... )")
            for row in grid:
                for spot in row:
                    spot.update_neighbours(grid)
            node_path = algorithm(lambda: draw(
                win, grid, ROWS, MAZE_WIDTH), grid, Start, End, counter_start)
            if node_path:  # Nếu tìm thấy đường đi
                time_elapsed, cells_visited, path_count = reconstruct_path(
                    node_path, End, draw, counter_start, win, grid, ROWS, MAZE_WIDTH)
                result_message = (
                    "Result:\n"
                    f"Time Elapsed: {format(time_elapsed, '.2f')}s\n"
                    f"Cells Visited: {cells_visited}\n"
                    f"Shortest Path: {path_count} Cells"
                )
            else:
                result_message = "Result:\n Path not found!"

    def clear_grid():
        nonlocal Start, End, grid, result_message
        Start = None
        End = None
        pygame.display.set_caption("Maze Solver ( Using A* Algorithm )")
        grid = make_grid(ROWS, MAZE_WIDTH)
        result_message = "Result:\n No result yet"

    def generate_maze():
        nonlocal grid, Start, End, result_message
        Start = None
        End = None
        generate_maze_dfs(grid, ROWS)
        result_message = "Result:\n No result yet"

    while Run:
        # Draw maze
        draw(win, grid, ROWS, MAZE_WIDTH)
        # Draw sidebar
        pygame.draw.rect(win, (164, 226, 153), (MAZE_WIDTH, 0,
                         WINDOW_WIDTH - MAZE_WIDTH, HEIGHT))
        # Draw buttons in the sidebar  
        draw_button(win, MAZE_WIDTH + 45, 20, 250, 40, "Solve", start_algorithm)
        draw_button(win, MAZE_WIDTH + 45, 80, 250, 40, "Clear", clear_grid)
        draw_button(win, MAZE_WIDTH + 45, 140, 250, 40, "Generate Maze", generate_maze)
        draw_button(win, MAZE_WIDTH + 45, 200, 250, 40, "Instruction", show_instructions)
        # Draw Result box
        draw_result_box(win, result_message, MAZE_WIDTH)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                Run = False
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if pos[1] < HEIGHT and pos[0] < MAZE_WIDTH:
                    row, col = get_mouse_pos(pos, ROWS, MAZE_WIDTH)
                    spot = grid[row][col]
                    if spot.is_wall():
                        display_message(
                            win, "Cannot select Start or End on a wall!", FONT)
                        continue
                    if not Start and spot != End:
                        Start = spot
                        Start.make_start()
                    elif not End and spot != Start:
                        End = spot
                        End.make_end()
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                if pos[1] < HEIGHT and pos[0] < MAZE_WIDTH:
                    row, col = get_mouse_pos(pos, ROWS, MAZE_WIDTH)
                    spot = grid[row][col]
                    spot.reset()
                    if spot == Start:
                        Start = None
                    if spot == End:
                        End = None
        pygame.display.update()
    pygame.quit()
    
if __name__ == "__main__":
    main()
