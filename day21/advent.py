with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

monkeys = {line[0:4]: line[6:] for line in lines}

ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}


def solve1():
    monkes = monkeys.copy()
    names = list(monkes.keys())
    i = 0

    while True:
        if (monkes['root'].isnumeric()):
            break

        name = names[i]
        num = monkes[names[i]]
        if not num[-1].isnumeric():
            monkey1, op, monkey2 = num.split(' ')
            if monkes[monkey1].isnumeric() and monkes[monkey2].isnumeric():
                monkes[name] = str(int(ops[op](int(monkes[monkey1]), int(monkes[monkey2]))))
        i = (i + 1) % (len(names))
    return monkes['root']

answer1 = solve1()
print(answer1)
print(monkeys)