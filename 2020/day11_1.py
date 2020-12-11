import fileinput

grid = list(row.strip() for row in fileinput.input())


def neighs(i, j):
    if i > 0:
        yield grid[i - 1][j]
    if i < len(grid) - 1:
        yield grid[i + 1][j]
    if i > 0 and j > 0:
        yield grid[i - 1][j - 1]
    if i < len(grid) - 1 and j < len(grid[0]) - 1:
        yield grid[i + 1][j + 1]
    if i > 0 and j < len(grid[0]) - 1:
        yield grid[i - 1][j + 1]
    if i < len(grid) - 1 and j > 0:
        yield grid[i + 1][j - 1]
    if j > 0:
        yield grid[i][j - 1]
    if j < len(grid[0]) - 1:
        yield grid[i][j + 1]


while True:
    new_grid = [
        [
            "#"
            if cell == "L" and all(n != "#" for n in neighs(i, j))
            else "L"
            if cell == "#" and sum(1 for n in neighs(i, j) if n == "#") > 3
            else cell
            for j, cell in enumerate(row)
        ]
        for i, row in enumerate(grid)
    ]
    if all(r1 == r2 for r1, r2 in zip(grid, new_grid)):
        break
    else:
        grid = new_grid

print(sum(1 for row in grid for i in row if i == "#"))
