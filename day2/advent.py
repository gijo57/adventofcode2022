points = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'draw': 3,
    'win': 6
}

comparisons = {
    'A': {
        'win': 'Y',
        'draw': 'X',
        'lose': 'Z'
    },
    'B': {
        'win': 'Z',
        'draw': 'Y',
        'lose': 'X'
    },
    'C': {
        'win': 'X',
        'draw': 'Z',
        'lose': 'Y'
    }
}


with open('input.txt', 'r') as f:
    rounds = [round.rstrip().split(' ') for round in f.readlines()]


def solve1(rounds):
    result = 0
    for round in rounds:
        result = result + points[round[1]]
        if round[1] == comparisons[round[0]]['win']:
            result = result + points['win']
        elif round[1] == comparisons[round[0]]['draw']:
            result = result + points['draw']
    return result


def solve2(rounds):
    result = 0
    for round in rounds:
        if round[1] == 'X':
            result = result + points[comparisons[round[0]]['lose']]
        elif round[1] == 'Y':
            result = result + points[comparisons[round[0]]['draw']] + points['draw']
        elif round[1] == 'Z':
            result = result + points[comparisons[round[0]]['win']] + points['win']
    return result


answer1, answer2 = solve1(rounds), solve2(rounds)
print(answer1, answer2)
