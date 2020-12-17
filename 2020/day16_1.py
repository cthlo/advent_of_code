import fileinput

with fileinput.input() as f:
    ranges = [
        range(int(lb), int(ub) + 1)
        for rule in iter(lambda: next(f).strip(), "")
        for rng in rule.split(": ")[1].split(" or ")
        for lb, ub in [rng.split("-")]
    ]
    for _ in range(4):
        next(f)

    total = 0
    for ticket in f:
        for val_s in line.split(","):
            val_i = int(val_s)
            if not any(val_i in r for r in ranges):
                total += val_i

print(total)
