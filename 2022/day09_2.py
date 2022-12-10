import fileinput

l: list[tuple[int, int]] = [(0, 0)] * 10
visited: set[tuple[int, int]] = {(0, 0)}
offset: dict[str, tuple[int, int]] = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0),
}


def add(a: tuple[int, int], b: tuple[int, int]):
    return a[0] + b[0], a[1] + b[1]


for line in fileinput.input():
    dir, count = line.split()
    for _ in range(int(count)):
        l[0] = add(l[0], offset[dir])
        for i in range(1, 10):
            d = tuple(b - a for a, b in zip(l[i], l[i - 1]))
            if any(abs(n) >= 2 for n in d):
                l[i] = add(l[i], tuple(n // abs(n) if n != 0 else 0 for n in d))
        visited.add(l[9])

print(len(visited))
