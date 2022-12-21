from ast import literal_eval

with open('example.txt') as f:
    pairs = [[literal_eval(item) for item in pair.split('\n')] for pair in f.read().split('\n\n')]
