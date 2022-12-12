import fileinput
from collections import deque

Pos = tuple[int, int]


map = [[ord(c) for c in line.strip()] for line in fileinput.input()]
start = next(
    (i, j)
    for i, row in enumerate(map)
    for j, cell in enumerate(row)
    if cell == 83  # ord("S")
)
end = next(
    (i, j)
    for i, row in enumerate(map)
    for j, cell in enumerate(row)
    if cell == 69  # ord("E")
)
map[start[0]][start[1]] = ord("a")
map[end[0]][end[1]] = ord("z")
visited: set[Pos] = set()


def neighs(pos: Pos):
    i, j = pos
    cell = map[i][j]
    if i > 0 and cell + 1 >= map[i - 1][j]:
        yield (i - 1, j)
    if i < len(map) - 1 and cell + 1 >= map[i + 1][j]:
        yield (i + 1, j)
    if j > 0 and cell + 1 >= map[i][j - 1]:
        yield (i, j - 1)
    if j < len(map[0]) - 1 and cell + 1 >= map[i][j + 1]:
        yield (i, j + 1)


q: deque[tuple[Pos, int]] = deque([(start, 0)])
while True:
    curr, steps = q.popleft()
    if curr == end:
        break
    if curr in visited:
        continue
    visited.add(curr)
    for i, j in neighs(curr):
        if (i, j) not in visited:
            q.append(((i, j), steps + 1))

print(steps)
