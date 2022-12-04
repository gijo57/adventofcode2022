with open('input.txt', 'r') as f:
    sections = [section.split(',') for section in f.read().split('\n')]


def solve1():
    result = 0
    for section in sections:
        elf1, elf2 = section[0].split('-'), section[1].split('-')
        if (int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1])) or (int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1])):
            result += 1
    return result


def solve2():
    result = 0
    for section in sections:
        elf1, elf2 = section[0].split('-'), section[1].split('-')
        if int(elf1[0]) <= int(elf2[1]) and int(elf1[1]) >= int(elf2[0]):
            print(section)
            result += 1
    return result


answer1, answer2 = solve1(), solve2()
print(answer1, answer2)
