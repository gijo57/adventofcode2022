with open('example.txt') as f:
    movements = [movement.strip().split(' ') for movement in f.readlines()]
    head_positions = [(0, 0)]
    tail_positions = [(0, 0)]


def calculate_diagonal(current_tail_position, head_position, direction):
    if (current_tail_position[1] != head_position[1] and current_tail_position[0] != head_position[0]):
        if direction == 'U':
            new_pos = current_tail_position[0]+1 if head_position[0] > current_tail_position[0] else current_tail_position[0]-1
            pos_after_diagonal_move = (new_pos, current_tail_position[1]+1)
            tail_positions.append(pos_after_diagonal_move)
            return pos_after_diagonal_move
        if direction == 'D':
            new_pos = current_tail_position[0]-1 if head_position[0] > current_tail_position[0] else current_tail_position[0]-1
            pos_after_diagonal_move = (new_pos, current_tail_position[1]-1)
            tail_positions.append(pos_after_diagonal_move)
            return pos_after_diagonal_move
        if direction == 'L':
            new_pos = current_tail_position[1]-1 if head_position[1] > current_tail_position[1] else current_tail_position[1]-1
            pos_after_diagonal_move = (current_tail_position[0]-1, new_pos)
            tail_positions.append(pos_after_diagonal_move)
            return pos_after_diagonal_move
        if direction == 'R':
            new_pos = current_tail_position[1]+1 if head_position[1] > current_tail_position[1] else current_tail_position[1]-1
            pos_after_diagonal_move = (current_tail_position[0]+1, new_pos)
            tail_positions.append(pos_after_diagonal_move)
            return pos_after_diagonal_move
    return current_tail_position


def calculate_tail_positions(current_tail_position, head_position, direction):
    tail_positions = []

    current_tail_position = calculate_diagonal(current_tail_position, head_position, direction)

    if current_tail_position[1] == head_position[1]:
        for pos in range(abs(head_position[0] - current_tail_position[0])):
            new_pos = pos + current_tail_position[0] if direction == 'R' else -pos + current_tail_position[0] if direction == 'L' else pos
            tail_positions.append((new_pos, current_tail_position[1]))
    if current_tail_position[0] == head_position[0]:
        for pos in range(abs(head_position[1] - current_tail_position[1])):
            new_pos = pos + current_tail_position[1] if direction == 'U' else -pos + current_tail_position[1] if direction == 'D' else pos
            tail_positions.append((current_tail_position[0], new_pos))
    return tail_positions


def calculate_head_position(direction, steps, current_head_pos):
        if direction == 'R':
            new_head_position = (current_head_pos[0] + steps, current_head_pos[1])
        elif direction == 'L':
            new_head_position = (current_head_pos[0] - steps, current_head_pos[1])
        elif direction == 'U':
            new_head_position = (current_head_pos[0], current_head_pos[1] + steps)
        elif direction == 'D':
            new_head_position = (current_head_pos[0], current_head_pos[1] - steps)
        return new_head_position


def solve1():
    for movement in movements:
        current_tail_pos, current_head_pos = tail_positions[-1], head_positions[-1]
        direction, steps = movement[0], int(movement[1])
        new_head_position = calculate_head_position(direction, steps, current_head_pos)
        head_positions.append(new_head_position)
        new_tail_positions = calculate_tail_positions(current_tail_pos, new_head_position, direction)
        tail_positions.extend(new_tail_positions)
        if tail_positions[-1] == head_positions[-1]:
            tail_positions.pop()
        print('head', head_positions)
        print('tail', tail_positions)
    return len(set(tail_positions))

answer1 = solve1()
print(answer1)
