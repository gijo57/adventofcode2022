with open('input.txt') as f:
    buffer = f.readline()


def solve(buffer, marker_length):
    for i, char in enumerate(buffer):
        marker = set(buffer[i:i+marker_length])
        if (len(marker) == marker_length):
            result = i+marker_length
            break
    return result


answer1, answer2 = solve(buffer, 4), solve(buffer, 14)
print(answer1, answer2)
