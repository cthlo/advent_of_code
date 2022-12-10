import fileinput
from typing import Iterable

grid = [line.strip() for line in fileinput.input()]
m = len(grid)
n = len(grid[0])
visible: set[tuple[int, int]] = set()


def count(trees: Iterable[tuple[int, int]]):
    max_so_far = ""
    for i, j in trees:
        if grid[i][j] > max_so_far:
            max_so_far = grid[i][j]
            visible.add((i, j))


for i in range(m):
    count((i, j) for j in range(n))
    count((i, j) for j in reversed(range(n)))

for j in range(n):
    count((i, j) for i in range(m))
    count((i, j) for i in reversed(range(m)))

print(len(visible))
