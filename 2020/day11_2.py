import fileinput

grid = list(row.strip() for row in fileinput.input())


def neighs(i, j):
    yield next(
        (grid[m][j] for m in reversed(range(i)) if grid[m][j] in ["#", "L"]), None
    )
    yield next(
        (grid[m][j] for m in range(i + 1, len(grid)) if grid[m][j] in ["#", "L"]), None
    )
    yield next(
        (grid[i][n] for n in reversed(range(j)) if grid[i][n] in ["#", "L"]), None
    )
    yield next(
        (grid[i][n] for n in range(j + 1, len(grid[0])) if grid[i][n] in ["#", "L"]),
        None,
    )

    yield next(
        (
            grid[m][n]
            for m, n in zip(reversed(range(i)), reversed(range(j)))
            if grid[m][n] in ["#", "L"]
        ),
        None,
    )
    yield next(
        (
            grid[m][n]
            for m, n in zip(range(i + 1, len(grid)), reversed(range(j)))
            if grid[m][n] in ["#", "L"]
        ),
        None,
    )
    yield next(
        (
            grid[m][n]
            for m, n in zip(reversed(range(i)), range(j + 1, len(grid[0])))
            if grid[m][n] in ["#", "L"]
        ),
        None,
    )
    yield next(
        (
            grid[m][n]
            for m, n in zip(range(i + 1, len(grid)), range(j + 1, len(grid[0])))
            if grid[m][n] in ["#", "L"]
        ),
        None,
    )


while True:
    new_grid = [
        [
            "#"
            if cell == "L" and all(n != "#" for n in neighs(i, j))
            else "L"
            if cell == "#" and sum(1 for n in neighs(i, j) if n == "#") > 4
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
