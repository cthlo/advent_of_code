import fileinput
from functools import reduce

deltas = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

counts = [0] * len(deltas)
for y, line in enumerate(fileinput.input()):
    n = len(line) - 1
    for i, (dx, dy) in enumerate(deltas):
        if y % dy == 0 and line[dx * y // dy % n] == "#":
            counts[i] += 1

print(reduce(lambda a, b: a * b, counts))
