import fileinput
import re
from collections import defaultdict
from itertools import takewhile

inp = fileinput.input()

crates: dict[int, list[str]] = defaultdict(list)
for line in takewhile(lambda line: line != "\n", inp):
    for i in range(1, len(line), 4):
        if (crate := line[i]).isalpha():
            crates[i // 4 + 1].append(crate)

for line in inp:
    n, f, t = [int(s) for s in re.findall(r"\d+", line)]
    crates[t] = crates[f][:n] + crates[t]
    crates[f] = crates[f][n:]


print("".join(crates[i][0] for i in range(1, len(crates) + 1)))
