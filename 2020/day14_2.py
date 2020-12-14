import fileinput
from itertools import product


def offsets(off):
    n = ["0"] * 36
    for o in product(["0", "1"], repeat=len(off)):
        for j, v in zip(off, o):
            n[j] = v
        yield int("".join(n), 2)


mem = {}
for line in fileinput.input():
    lhs, rhs = line.strip().split(" = ")
    if lhs == "mask":
        mask = rhs
        offs = list(offsets([i for i, m in enumerate(mask) if m == "X"]))
    else:
        addr = int(lhs.split("[")[1][:-1])
        base = int(
            "".join(
                ("0" if m == "X" else "1" if m == "1" else v)
                for m, v in zip(mask, bin(addr)[2:].zfill(36))
            ),
            2,
        )
        for o in offs:
            mem[o + base] = int(rhs)

print(sum(v for _, v in mem.items()))
