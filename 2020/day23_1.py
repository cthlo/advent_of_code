import fileinput

cups = list(int(i) for i in next(fileinput.input()).strip())
n = len(cups)
m = max(cups)

curr = cups[0]
for _ in range(100):
    # three cups
    curr_idx = cups.index(curr)
    three = (cups + cups)[curr_idx + 1 : curr_idx + 4]

    # next dest
    dest = curr
    while (dest := dest - 1 if dest > 1 else n) in three:
        pass

    # move three cups
    for t in three:
        cups.remove(t)
    nn = cups.index(dest) + 1
    cups = cups[:nn] + three + cups[nn:]

    # next curr
    curr = cups[(cups.index(curr) + 1) % n]

one_idx = cups.index(1)
print("".join(str(v) for v in cups[one_idx + 1 :] + cups[:one_idx]))
