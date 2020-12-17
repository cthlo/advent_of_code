import fileinput
from itertools import product

space = {
    (i, j, 0, 0)
    for i, row in enumerate(fileinput.input())
    for j, v in enumerate(row)
    if v == "#"
}

prods = [p for p in product([-1, 0, 1], repeat=4) if p != (0, 0, 0, 0)]


def neighs(i, j, k, l):
    for x, y, z, w in prods:
        yield (i + x, j + y, k + z, l + w)


for _ in range(6):
    all_active = space
    all_neighs = {n for c in space for n in neighs(*c) if n not in space}

    new_space = set()
    for c in all_active:
        if sum(1 for n in neighs(*c) if n in space) in [2, 3]:
            new_space.add(c)
    for c in all_neighs:
        if sum(1 for n in neighs(*c) if n in space) == 3:
            new_space.add(c)

    space = new_space

print(len(space))
