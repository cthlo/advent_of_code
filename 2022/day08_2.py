import fileinput
from collections import defaultdict
from typing import Iterable

grid = [line.strip() for line in fileinput.input()]
m = len(grid)
n = len(grid[0])
scores: defaultdict[tuple[int, int], int] = defaultdict(lambda: 1)


def count(trees: Iterable[tuple[int, int]]):
    l: list[tuple[str, int]] = []
    for i, j in trees:
        curr_h, curr_v = grid[i][j], 1 if l else 0
        while l and l[-1][0] < curr_h:
            curr_v += l.pop()[1]
        l.append((curr_h, curr_v))
        scores[(i, j)] *= curr_v


for i in range(m):
    count((i, j) for j in range(n))
    count((i, j) for j in reversed(range(n)))

for j in range(n):
    count((i, j) for i in range(m))
    count((i, j) for i in reversed(range(m)))

print(max(scores.values()))
