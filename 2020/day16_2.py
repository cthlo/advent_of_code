import fileinput
from functools import reduce

with fileinput.input() as f:
    fields = {
        field: [
            range(int(lb), int(ub) + 1)
            for r in rng.split(" or ")
            for lb, ub in [r.split("-")]
        ]
        for rule in iter(lambda: next(f).strip(), "")
        for field, rng in [rule.split(": ")]
    }
    next(f)
    my_tic = [int(s) for s in next(f).split(",")]
    next(f)
    next(f)

    tickets = list([int(s) for s in line.split(",")] for line in f)

ranges = [r for rngs in fields.values() for r in rngs]
valid_tickets = [
    tic for tic in tickets if all(any(v in r for r in ranges) for v in tic)
]

cols = dict(enumerate(zip(*valid_tickets)))
pos = {}
while fields:
    for i, c in cols.items():
        cands = [
            f for f, rngs in fields.items() if all(any(v in r for r in rngs) for v in c)
        ]
        # input is a simple case, i.e. there is one column that's only valid for one specific field
        if len(cands) == 1:
            f = cands[0]
            pos[f] = i
            del fields[f]
            del cols[i]
            break

print(
    reduce(
        lambda x, y: x * y,
        (my_tic[i] for f, i in pos.items() if f.startswith("departure ")),
    )
)
