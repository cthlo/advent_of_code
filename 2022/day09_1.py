import fileinput

t = h = (0, 0)
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
        new_h = add(h, offset[dir])
        if any(abs(a - b) >= 2 for a, b in zip(t, new_h)):
            visited.add(t := h)
        h = new_h

print(len(visited))
