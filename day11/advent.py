with open('input.txt') as f:
    monkeys = [[stripped_monkey.strip() for stripped_monkey in monkey.split('\n')] for monkey in f.read().split('\n\n')]
    monkey_dict = {}


def solve1():
    ops = {
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y
    }

    for monkey in monkeys:
        name = monkey[0][-2]
        items = [int(item.strip()) for item in monkey[1].split(':')[1].split(',')]
        operation = [part.strip() for part in monkey[2].split('=')[1].split(' ') if part != '']
        test_divisor = int(monkey[3].split(' ')[-1])
        true_val = monkey[4].split(' ')[-1]
        false_val = monkey[5].split(' ')[-1]
        monkey_dict[name] = {
            'items': items,
            'operation': operation,
            'test_divisor': test_divisor,
            'true_val': true_val,
            'false_val': false_val,
        }

    inspects = [0 for _ in range(len(monkeys))]

    for round in range(20):
        for monkey in monkey_dict.keys():
            current_monkey = monkey_dict[monkey]
            for item in current_monkey['items']:
                op_val = item if current_monkey['operation'][2] == 'old' else int(current_monkey['operation'][2])
                new_worry_level = (ops[current_monkey['operation'][1]](item, int(op_val))) // 3
                target_monkey = current_monkey['true_val'] if new_worry_level % current_monkey['test_divisor'] == 0 else current_monkey['false_val']
                monkey_dict[target_monkey]['items'].append(new_worry_level)
                inspects[int(monkey)] += 1
            current_monkey['items'] = []

    inspects.sort()

    return inspects[-2] * inspects[-1]


answer1 = solve1()
print(answer1)