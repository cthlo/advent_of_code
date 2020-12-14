import fileinput

mem = {}
for line in fileinput.input():
    lhs, rhs = line.strip().split(" = ")
    if lhs == "mask":
        mask = rhs
    else:
        addr = int(lhs.split("[")[1][:-1])
        mem[addr] = int(
            "".join(
                m if m != "X" else v for m, v in zip(mask, bin(int(rhs))[2:].zfill(36))
            ),
            2,
        )

print(sum(v for _, v in mem.items()))
