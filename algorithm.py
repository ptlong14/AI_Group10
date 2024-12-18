
from queue import PriorityQueue
from timeit import default_timer as timer
from node import Node
import pygame
pygame.init()


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(node_path, current, draw, counter_start, win, grid, rows, width):
    path_count = 0
    while current in node_path:
        current = node_path[current]
        current.make_path()
        path_count += 1
        draw(win, grid, rows, width)
    time_elapsed = timer() - counter_start
    pygame.display.set_caption(f'Time Elapsed: {format(time_elapsed, ".2f")}s | Cells Visited: {
                               len(node_path) + 1} | Shortest Path: {path_count + 1} Cells')
    return time_elapsed, len(node_path) + 1, path_count + 1


def algorithm(draw, grid, start, end, counter_start):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    node_path = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
    open_set_hash = {start}

    while not open_set.empty():
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            return node_path

        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbour]:
                node_path[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + \
                    h(neighbour.get_pos(), end.get_pos())
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()

        draw()
        if current != start:
            current.make_close()

    pygame.display.set_caption(
        "Maze Solver ( Unable To Find The Target Node ! )")
    return {}
