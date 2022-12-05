import copy

with open('example.txt', 'r') as f:
    stacks, instructions = f.read().split('\n\n')
    instructions = instructions.split('\n')
    stacks = [[item for item in stack.replace('    ', '_'). replace(' ', '')] for stack in stacks.replace('[', '').replace(']', '').split('\n')]
    formatted_stacks = [[] for _ in range(int(stacks[-1][-1]))]

    for stack in stacks[:-1]:
        for i, item in enumerate(stack):
            if item != '_':
                formatted_stacks[i].insert(0, item)

    formatted_stacks2 = copy.deepcopy(formatted_stacks)
    for instruction in instructions:
        qty, from_stack, to_stack = [int(val) for val in instruction.split() if val.isdigit()]
        formatted_stacks2[to_stack-1].extend(formatted_stacks2[from_stack-1][-qty:])
        formatted_stacks2[from_stack-1] = formatted_stacks2[from_stack-1][:-qty]
        for crate in range(qty):
            formatted_stacks[to_stack-1].append(formatted_stacks[from_stack-1].pop())

    answer1 = ''
    for stack in formatted_stacks:
        answer1 += stack[-1]

    answer2 = ''
    for stack in formatted_stacks2:
        answer2 += stack[-1]

print(answer1, answer2)