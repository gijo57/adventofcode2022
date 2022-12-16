import itertools

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    stack, dir_sizes = [], []

for line in lines:
    print('line', line, 'stack', stack)
    if line.startswith('$ cd ..'):
        size = stack.pop()
        dir_sizes.append(size)
        stack[-1] += size
    elif line.startswith('$ cd '):
        stack.append(0)
    elif line[0].isdigit():
        stack[-1] += int(line.split()[0])

dir_sizes.extend(itertools.accumulate(stack[::-1]))

print(sum(x for x in dir_sizes if x <= 100000))
print(min(x for x in dir_sizes if x >= max(dir_sizes) - 40000000))
