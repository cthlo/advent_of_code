import fileinput
from collections import defaultdict
from itertools import chain
from typing import Callable

inp = fileinput.input()


def takewhile(predicate: Callable[[str], bool]):
    global inp
    for line in inp:
        if predicate(line):
            yield line
        else:
            inp = chain([line], inp)
            break


curr: tuple[str, ...] = ()
dirs: set[str] = set()
sizes: defaultdict[tuple[str, ...], int] = defaultdict(int)

while line := next(inp, None):
    parts = line.split()
    if parts[1] == "cd":
        if parts[2] == "..":
            curr = curr[:-1]
        elif parts[2] == "/":
            curr = ()
        else:
            curr += (parts[2],)
    else:
        for ls_line in takewhile(lambda l: l[0] != "$"):
            size_or_dir, f = ls_line.split()
            if size_or_dir == "dir":
                sizes.setdefault(curr + (f,), 0)
            elif curr not in dirs:
                for i in range(len(curr), -1, -1):
                    sizes[curr[:i]] += int(size_or_dir)


print(sum(size for size in sizes.values() if size <= 100000))
