from ast import literal_eval

with open('example.txt') as f:
    pairs = [[literal_eval(item) for item in pair.split('\n')] for pair in f.read().split('\n\n')]


def compare_values(value1, value2):
    if isinstance(value1, int) and isinstance(value2, int):
        return value1 < value2
    else:
        # for-loop
        value1 = [value1] if isinstance(value1, int) else value1
        value2 = [value2] if isinstance(value2, int) else value2

        if len(value1) == 0:
            return True
        if len(value2) == 0:
            return False
        return compare_values(value1[0], value2[0])


def compare_packets(pair1, pair2):
    len1 = len(pair1)
    len2 = len(pair2)
    comparison = None

    if (len1 > len2):
        for i in range(len2):
            comparison = compare_values(pair1[i], pair2[i])
            if comparison:
                break
    else:
        for i in range(len1):
            comparison = compare_values(pair1[i], pair2[i])
            if comparison:
                break
    return comparison


correct_indices = []
for i, pair in enumerate(pairs):
    pair_comparison = compare_packets(pair[0], pair[1])
    print(pair_comparison)
    if pair_comparison:
        correct_indices.append(i+1)

print(correct_indices)
