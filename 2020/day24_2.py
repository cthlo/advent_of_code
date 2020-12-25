import fileinput
from collections import defaultdict


def neighs(t):
    x, y = t
    return {
        "e": (x + 1, y + 0.5),
        "se": (x + 1, y - 0.5),
        "sw": (x, y - 1),
        "w": (x - 1, y - 0.5),
        "nw": (x - 1, y + 0.5),
        "ne": (x, y + 1),
    }


tiles = {}
ref = (0, 0)
for line in fileinput.input():
    line = line.strip()
    t = ref
    while line:
        (d, t) = next((d, n) for d, n in neighs(t).items() if line.startswith(d))
        line = line[len(d) :]
    tiles[t] = not tiles.get(t)


for _ in range(100):
    for t in list(tiles):
        for n in neighs(t).values():
            tiles[n] = tiles.get(n)

    new_tiles = {}
    for t in tiles:
        blk_neighs = sum(1 for n in neighs(t).values() if tiles.get(n))
        t_color = tiles.get(t)
        if not t_color and blk_neighs == 2:
            new_tiles[t] = True
        elif t_color and 0 < blk_neighs < 3:
            new_tiles[t] = True
    tiles = new_tiles

print(sum(1 for c in tiles.values() if c))
