with open('input.txt') as f:
    original_message = [(i, int(num)) for i, num in enumerate(f.readlines())]


def mix(original_message, message):
    for item in original_message:
        old_i = message.index(item)
        new_i = (old_i + item[1]) % (len(original_message) - 1)
        message.pop(old_i)
        message.insert(new_i if new_i else len(message), item)


def calculate_result(message):
    values = [val[1] for val in message]
    zero = values.index(0)
    result = 0

    for i in range(3001):
        index = (i + zero) % len(values)
        if i in [1000, 2000, 3000]:
            result += values[index]
    return result


def solve1():
    message = original_message.copy()
    mix(original_message, message)
    return calculate_result(message)


def solve2():
    original_message2 = [(i, val * 811589153) for i, val in original_message]
    message = original_message2.copy()

    for _ in range(10):
        mix(original_message2, message)
    return calculate_result(message)


answer1, answer2 = solve1(), solve2()
print(answer1, answer2)
