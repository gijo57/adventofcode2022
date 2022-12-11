import numpy as np

with open('input.txt') as f:
    instructions = [instruction.strip().split(' ') for instruction in f.readlines()]


def solve1(instructions):
    prev_cycle = 1
    cycle = 1
    last_significant_cycle = 20
    x = 1
    signal_strengths = []

    for instruction in instructions:
        prev_cycle = cycle
        if instruction[0] == 'noop':
            cycle += 1
            continue
        val = int(instruction[1])
        cycle += 2
        if prev_cycle <= last_significant_cycle <= cycle:
            if last_significant_cycle == cycle:
                x += val
                signal_strengths.append(last_significant_cycle * x)
                last_significant_cycle += 40
                x -= val
            else:
                signal_strengths.append(last_significant_cycle * x)
                last_significant_cycle += 40
        x += val

    result = sum(signal_strengths)
    return result


def solve2(instructions):
    screen = [list("."*40) for _ in range(6)]
    x = 1
    op_index = 0
    cycle = 0
    cycles_passed = 1

    for _ in range(6*40):
        row = cycle // 40
        col = cycle - (row * 40)
        if cycle - 1 <= (x + (row * 40)) <= cycle + 1:
            screen[row][col] = "#"
        if instructions[op_index][0] != 'noop' and cycles_passed == 2:
            x += int(instructions[op_index][1])
            cycles_passed = 0
            op_index += 1
        elif instructions[op_index][0] == 'noop':
            cycles_passed = 0
            op_index += 1
        cycle += 1
        cycles_passed += 1
    return np.array(screen)


answer1 = solve1(instructions)
answer2 = solve2(instructions)
print(answer1, answer2)
