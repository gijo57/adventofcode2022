import numpy as np

with open('example.txt') as f:
    trees_map = [[int(tree) for tree in list(row.strip())] for row in f.readlines()]
    outer_count = (len(trees_map)-1)*4
    checked_trees = np.zeros((len(trees_map), len(trees_map)))


def check_direction(trees, checked, direction):
    for i, row in enumerate(trees[1:-1]):
        highest_tree = trees[i+1][0]
        for j, tree in enumerate(row[1:-1]):
            if tree > highest_tree:
                checked[i+1][j+1] = 1
                highest_tree = tree
    if direction == 'left':
        checked_trees = np.fliplr(checked)
    elif direction == 'down':
        checked_trees = np.rot90(checked, k=-1)
    elif direction == 'up':
        checked_trees = np.fliplr(np.rot90(checked, k=-1))
    else:
        return checked
    return checked_trees


def solve1(checked_trees):
    checked_trees = check_direction(np.array(trees_map), checked_trees, 'right')
    checked_trees = check_direction(np.fliplr(trees_map), np.fliplr(checked_trees), 'left')
    checked_trees = check_direction(np.rot90(trees_map), np.rot90(checked_trees), 'down')
    checked_trees = check_direction(np.fliplr(np.rot90(trees_map)), np.fliplr(np.rot90(checked_trees)), 'up')

    result = outer_count + int(np.sum(checked_trees))
    return result


def solve2():
    for i in range(len(trees_map)):
        for j in range(len(trees_map[0])):
            score = calc_scenic_score(i, j, trees_map)

            highest_score = score if score > highest_score else highest_score

    return highest_score


answer1 = solve1(checked_trees)
answer2 = solve2(trees_map)
print(answer1, answer2)
