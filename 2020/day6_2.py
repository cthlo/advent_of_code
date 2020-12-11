import fileinput
from functools import reduce

total = 0
with fileinput.input() as f:
    while True:
        lines = [set(line) for line in iter(lambda: next(f).strip(), "")]
        if len(lines) == 0:
            break

        total += len(reduce(lambda a, b: a.intersection(b), lines))

print(total)
