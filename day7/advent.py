with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    path = []


def map_dir_contents():
    directories = {}
    for line in lines:
        if 'cd' in line:
            if '..' in line:
                path.pop()
            elif '/' in line:
                path = ['/']
            else:
                path.append(line[-1])
            pwd = path[-1]
        elif '$' not in line:
            if 'dir' in line:
                item = line[-1]
            else:
                item = int(line.split(' ')[0])
            if pwd not in directories:
                directories[pwd] = []
                directories[pwd].append(item)
            else:
                directories[pwd].append(item)
    return directories


def sum_dir_files(directories):
    for dir in directories:
        if not isinstance(directories[dir], int):
            if all(isinstance(item, int) for item in directories[dir]):
                directories[dir] = sum(directories[dir])

    if not all(isinstance(item, int) for item in list(directories.values())):
        for dir in directories:
            if isinstance(directories[dir], list):
                for i, item in enumerate(directories[dir]):
                    if isinstance(item, str):
                        if isinstance(directories[directories[dir][i]], int):
                            directories[dir][i] = directories[directories[dir][i]]
        sum_dir_files(directories)


directories = map_dir_contents()
sum_dir_files(directories)
answer1 = sum([val for val in directories.values() if val <= 100000])
print(answer1)
