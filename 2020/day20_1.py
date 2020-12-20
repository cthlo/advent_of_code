import fileinput

tiles = {}
with fileinput.input() as f:
    while tid := next(f, None):
        tiles[int(tid[5:-2])] = [
            line.strip() for line in iter(lambda: next(f).strip(), "")
        ]


def get_borders(tile):
    return [
        tile[0],
        tile[-1],
        "".join(s[0] for s in tile),
        "".join(s[-1] for s in tile),
    ]


b2t = {}
for tid, tile in tiles.items():
    for b in get_borders(tile):
        invariant = "".join(sorted([b, b[::-1]]))
        b2t.setdefault(invariant, []).append(tid)

answer = 1
edge_tiles = set()
for b, tids in b2t.items():
    if len(tids) == 1:
        tid = tids[0]
        if tid in edge_tiles:
            answer *= tid
        edge_tiles.add(tid)

print(answer)
