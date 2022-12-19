with open('input.txt') as f:
    points = [[[int(c) for c in y.split(',')] for y in z] for z in [x.strip().split(' -> ') for x in f.readlines()]]


def set_rocks():
    rocks = set()
    for point in points:
        for i in range(1, len(point)):
            p1, p2 = (point[i - 1], point[i])
            x1, y1 = (p1[0], p1[1])
            x2, y2 = (p2[0], p2[1])

            xrange = range(x1, x2 + 1) if x2 >= x1 else range(x2, x1 + 1)
            yrange = range(y1, y2 + 1) if y2 >= y1 else range(y2, y1 + 1)

            rocks.update({(x, y) for x in xrange for y in yrange})
    return rocks


original_rocks = set_rocks()
units = original_rocks.copy()
bottom_depth = max(y for (x, y) in units)
starting_point = (500, 0)
floor = bottom_depth + 2

def solve1():
    grain = starting_point
    grain_count = 0

    while True:
        if grain[1] == bottom_depth:
            break
        if (grain[0], grain[1]+1) not in units:
            grain = (grain[0], grain[1]+1)
            continue
        if (grain[0]-1, grain[1]+1) not in units:
            grain = (grain[0]-1, grain[1]+1)
            continue
        if (grain[0]+1, grain[1]+1) not in units:
            grain = (grain[0]+1, grain[1]+1)
            continue

        units.add(grain)
        grain_count += 1
        grain = starting_point
    return grain_count


units2 = original_rocks.copy()


def solve2():
    grain = starting_point
    grain_count = 0

    while True:
        if starting_point in units2:
            break
        if grain[1]+1 == floor:
            units2.add(grain)
            grain_count += 1
            grain = starting_point
            continue
        if (grain[0], grain[1]+1) not in units2:
            grain = (grain[0], grain[1]+1)
            continue
        if (grain[0]-1, grain[1]+1) not in units2:
            grain = (grain[0]-1, grain[1]+1)
            continue
        if (grain[0]+1, grain[1]+1) not in units2:
            grain = (grain[0]+1, grain[1]+1)
            continue

        units2.add(grain)
        grain_count += 1
        grain = starting_point
    return grain_count


answer1 = solve1()
answer2 = solve2()
print(answer1, answer2)
