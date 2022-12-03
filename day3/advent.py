with open('input.txt', 'r') as f:
    rucksacks = [rucksack for rucksack in f.read().split('\n')]
    split_rucksacks = [[rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]] for rucksack in rucksacks]
    groups = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]


def solve1():
    total_priority = 0
    for rucksack in split_rucksacks:
        item_in_both_compartments = ''.join(set(rucksack[0]).intersection(rucksack[1]))
        priority = ord(item_in_both_compartments) - 96 if item_in_both_compartments.islower() else ord(item_in_both_compartments) - 38
        total_priority += priority
    return total_priority


def solve2():
    total_priority = 0
    for group in groups:
        item_in_both_compartments = ''.join(set(group[0]).intersection(group[1], group[2]))
        priority = ord(item_in_both_compartments) - 96 if item_in_both_compartments.islower() else ord(item_in_both_compartments) - 38
        total_priority += priority
    return total_priority


answer1, answer2 = solve1(), solve2()
print(answer1, answer2)
