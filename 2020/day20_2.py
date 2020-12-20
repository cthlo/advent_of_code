import fileinput
from functools import reduce

tiles = {}
with fileinput.input() as f:
    while tid := next(f, None):
        tiles[int(tid[5:-2])] = [
            line.strip() for line in iter(lambda: next(f).strip(), "")
        ]


def get_borders(tile):
    return [
        tile[0],
        "".join(s[-1] for s in tile),
        tile[-1],
        "".join(s[0] for s in tile),
    ]


def rotate(tile):
    return ["".join(s) for s in list(zip(*tile[::-1]))]


def oris(tile):
    yield tile
    for _ in range(3):
        yield (tile := rotate(tile))
    yield (tile := tile[::-1])
    for _ in range(3):
        yield (tile := rotate(tile))


b2t = {}
for tid, tile in tiles.items():
    for o in oris(tile):
        for i, b in enumerate(get_borders(o)):
            b2t.setdefault((b, i), []).append((tid, o))


def stitch(tid, tile, bid):
    border = get_borders(tile)[bid]
    for t, o in b2t[(border, (bid + 2) % 4)]:
        if t != tid:
            return (t, o)


# find a corner tile
tid = next(
    tid
    for tid, tile in tiles.items()
    if sum(
        1 for i, b in enumerate(get_borders(tile)) if len(b2t[(b, (i + 2) % 4)]) == 1
    )
    == 2
)

# find orientation so that border 1, 2 are inner borders
tile = next(o for o in oris(tiles[tid]) if stitch(tid, o, 1) and stitch(tid, o, 2))

# fill puzzle left to right, top to bottom
puzz = [[tile]]
while True:
    row_start = tid

    # keep matching right tile
    while nxt := stitch(tid, tile, 1):
        tid, tile = nxt
        puzz[-1].append(tile)

    # next row
    tile = puzz[-1][0]
    tid = row_start
    nxt = stitch(tid, tile, 2)
    if nxt:
        tid, tile = nxt
        puzz.append([tile])
    else:
        break


def strip(tile):
    return [r[1:-1] for r in tile[1:-1]]


def merge(row):
    return reduce(lambda t1, t2: [a + b for a, b in zip(t1, t2)], row)


final = [r for row in puzz for r in merge(strip(tile) for tile in row)]

monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
m_offsets = [(i, j) for i, r in enumerate(monster) for j, c in enumerate(r) if c == "#"]
m_size = len(m_offsets)

# find monsters in all orientations of final
roughness = sum(r.count("#") for r in final)
for o in oris(final):
    for i, r in enumerate(o):
        for j, _ in enumerate(r):
            try:
                if all(o[i + mi][j + mj] == "#" for mi, mj in m_offsets):
                    roughness -= m_size
            except IndexError:
                pass

print(roughness)
