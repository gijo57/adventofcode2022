import numpy as np
import re
from copy import deepcopy

turn = {
        'R': lambda a: (a[1], -a[0]),
        'L': lambda a: (-a[1], a[0])
}

facing = {
        (0, 1): 0,
        (-1, 0): 1,
        (0, -1): 2,
        (1, 0): 3
}

lastx = {}
lasty = {}
firstx = {}
firsty = {}

def set_inside(phantom_cursor: np.ndarray, direction: tuple) -> np.ndarray:
    
    y, x = phantom_cursor

    if direction in [(0, 1), (0, -1)]:
        if x > lastx[y]:
            x = firstx[y]
        if x < firstx[y]:
            x = lastx[y]
    
    if direction in [(1, 0), (-1, 0)]:
        if y > lasty[x]:
            y = firsty[x]
        if y < firsty[x]:
            y = lasty[x]

    return np.array([y, x])


def move(steps: int, direction: tuple, current_pos: np.ndarray) -> np.ndarray:
    phantom_cursor = deepcopy(current_pos)
    cursor = deepcopy(current_pos)

    for _ in range(steps):
        phantom_cursor += np.array(direction)

        phantom_cursor = set_inside(phantom_cursor, direction)

        if mapping[phantom_cursor[0]][phantom_cursor[1]] == '#':
            return cursor

        cursor = deepcopy(phantom_cursor)

    return cursor


def starting_pos() -> np.ndarray:
    for i in range(len(mapping[0])):
        if mapping[0][i] != ' ':
            return np.array([0, i])

    return np.array([0, 0])

with open('input.txt', 'r') as f:
    mapping, instructions = f.read().rstrip().split('\n\n')

    mapping = np.array([[*x] for x in mapping.split('\n')], dtype=object)

orientation = (0, 1)
current_pos = starting_pos()

instructions_fin = [(int(x) if x.isnumeric() else x) for x in re.findall(r'(\d+|[RL])', instructions)]

for y, line in enumerate(mapping):
    for x, c in enumerate(line):
        if c != ' ':
            if y not in firstx:
                firstx[y] = x
            lastx[y] = x
            if x not in firsty:
                firsty[x] = y
            lasty[x] = y

for instruction in instructions_fin:
    # print(instruction)
    if isinstance(instruction, int):
        current_pos = move(instruction, orientation, current_pos)
    else:
        orientation = turn[instruction](orientation)

    print(current_pos, orientation)

print((current_pos[0] + 1) * 1000 + (current_pos[1] + 1) * 4 + facing[orientation])