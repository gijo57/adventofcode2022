with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

monkey_nums = {line[0:4]: line[6:] for line in lines}

ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}


def solve1():
    names = list(monkey_nums.keys())
    i = 0

    while True:
        if (monkey_nums['root'].isnumeric()):
            print(monkey_nums['root'])
            break

        name = names[i]
        num = monkey_nums[names[i]]
        if not num[-1].isnumeric():
            monkey1, op, monkey2 = num.split(' ')
            if monkey_nums[monkey1].isnumeric() and monkey_nums[monkey2].isnumeric():
                monkey_nums[name] = str(int(ops[op](int(monkey_nums[monkey1]), int(monkey_nums[monkey2]))))
        i = (i + 1) % (len(names))


answer1 = solve1()
