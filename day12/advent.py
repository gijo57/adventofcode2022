import numpy as np
from collections import deque

with open('input.txt') as f:
    grid = [list(row.strip()) for row in f.readlines()]
    rows, cols = len(grid), len(grid[0])

    start = (np.where(np.array(grid) == 'S')[0][0], np.where(np.array(grid) == 'S')[1][0])


def check_neighbors(row, col, visited, queue, nodes_in_next_layer):
    row_directions = [-1, +1, 0, 0]
    col_directions = [0, 0, +1, -1]

    for i in range(0, 4):
        n_row = row + row_directions[i]
        n_col = col + col_directions[i]
        if n_row < 0 or n_col < 0 or n_row >= rows or n_col >= cols:
            continue

        pos = 'a' if grid[row][col] == 'S' else 'z' if grid[row][col] == 'E' else grid[row][col]
        pos_height = ord(pos)
        neighbor_height = ord(grid[n_row][n_col])
        height_diff = neighbor_height - pos_height

        if visited[n_row][n_col] or height_diff > 1:
            continue

        queue.appendleft((n_row, n_col))
        visited[n_row][n_col] = True
        nodes_in_next_layer += 1
    return visited, queue, nodes_in_next_layer


def solve():
    step_count = 0
    nodes_in_current_layer = 1
    nodes_in_next_layer = 0
    reached_end = False
    visited = [[False for _ in range(cols)] for row in range(rows)]
    queue = deque()

    queue.appendleft((start[0], start[1]))
    visited[start[0]][start[1]] = True

    while len(queue) > 0:
        row, col = queue.pop()
        if grid[row][col] == 'E':
            reached_end = True
            break

        visited, queue, nodes_in_next_layer = check_neighbors(row, col, visited, queue, nodes_in_next_layer)
        nodes_in_current_layer -= 1

        if nodes_in_current_layer == 0:
            nodes_in_current_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            step_count += 1
    if reached_end:
        return step_count
    return


print(solve())
#ANSWER: 31 steps