with open('example.txt') as f:
    movements = [movement.strip().split(' ') for movement in f.readlines()]
    head_positions = [(0, 0)]
    tail_positions = [(0, 0)]


def calculate_tail_position(current_tail_position, head_position):
    pass


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


for movement in movements:
    current_tail_pos, current_head_pos = tail_positions[-1], head_positions[-1]
    direction, steps = movement[0], int(movement[1])
    new_head_position = calculate_head_position(direction, steps, current_head_pos)
    head_positions.append(new_head_position)
    new_tail_position = calculate_tail_position(current_tail_pos, new_head_position)



print(head_positions)
#There are 13 positions the tail visited at least once.
