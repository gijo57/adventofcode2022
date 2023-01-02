import numpy as np
import re

with open('example.txt') as f:
    parts = f.read().split('\n\n')
    board_data = [list(x) for x in parts[0].split('\n')]
    cols, rows = len(max(board_data, key=len)), len(board_data)
    board = [['_' for x in range(cols)] for y in range(rows)]

    for y, val in enumerate(board):
        for x, val in enumerate(board[y]):
            try:
                board[y][x] = board_data[y][x]
            except:
                board[y][x] = ' '

current_pos = np.array([0, board[0].index('.')])
instructions = re.split('(R|L)', parts[1])
direction = np.array([0, 1])

turn = {
    'R': lambda a: np.array([a[1], -a[0]]),
    'L': lambda a: np.array([-a[1], a[0]])
}


def wrap_around(row, col, direction):
    current_direction = 'vertical' if direction[0] == 1 else 'horizontal'
    col_data = list(np.array(board)[:, col])
    first_horizontal_index = min(board[row].index('.') if '.' in board[row] else -1, board[row].index('#')  if '#' in board[row] else -1)
    last_horizontal_index = max((loc for loc, val in enumerate(board[row]) if val != ' '), default=None)
    first_vertical_index = min(col_data.index('.') if '.' in col_data else -1, col_data.index('#')  if '#' in col_data else -1)
    last_vertical_index = max((loc for loc, val in enumerate(col_data) if val in ['.', '#']), default=None)

    if current_direction == 'horizontal':
        if col < first_horizontal_index:
            new_pos = np.array([row, last_horizontal_index])
            if board[new_pos[0]][new_pos[1]] == '.':
                return new_pos
            else:
                return np.array([row, col+1])
        if col > last_horizontal_index:
            new_pos = np.array([row, first_horizontal_index])
            if board[new_pos[0]][new_pos[1]] == '.':
                return new_pos
            else:
                return np.array([row, col-1])
    elif current_direction == 'vertical':
        if row < first_vertical_index:
            new_pos = np.array([last_vertical_index, col])
            if board[new_pos[0]][new_pos[1]] == '.':
                return new_pos
            else:
                return np.array([row+1, col])
        if row > last_vertical_index:
            new_pos = np.array([first_vertical_index, col])
            if board[new_pos[0]][new_pos[1]] == '.':
                return new_pos
            else:
                return np.array([row-1, col])



for instruction in instructions:
    if instruction in ['R', 'L']:
        direction = turn[instruction](direction)
    else:
        for _ in range(int(instruction)):
            new_pos = current_pos + direction
            new_pos = np.array([new_pos[0] % len(board), new_pos[1] % len(max(board_data, key=len))])

            if board[new_pos[0]][new_pos[1]] == ' ':
                new_pos = wrap_around(new_pos[0], new_pos[1], direction)
            if board[new_pos[0]][new_pos[1]] == '#':
                break
            current_pos = new_pos

directions = {
        (0, 1): 0,
        (-1, 0): 1,
        (0, -1): 2,
        (1, 0): 3
}

final_direction = directions[tuple(direction)]
answer1 = (current_pos[0]+1)*1000 + (current_pos[1]+1)*4 + final_direction
print(final_direction)
print(current_pos)
print(answer1)