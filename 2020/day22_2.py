import fileinput

with fileinput.input() as f:
    next(f)
    p1 = list(int(v) for v in iter(lambda: next(f).strip(), ""))
    next(f)
    p2 = list(int(v) for v in iter(lambda: next(f).strip(), ""))


def game(p1, p2):
    prev = set()
    while len(p1) > 0 and len(p2) > 0:
        conf = (tuple(p1), tuple(p2))
        if conf in prev:
            return (1, p1)
        prev.add(conf)

        if len(p1) > p1[0] and len(p2) > p2[0]:
            winner, _ = game(p1[1 : p1[0] + 1], p2[1 : p2[0] + 1])
        else:
            winner = 1 if p1[0] > p2[0] else 2

        if winner == 1:
            p1.extend([p1[0], p2[0]])
        else:
            p2.extend([p2[0], p1[0]])

        p1 = p1[1:]
        p2 = p2[1:]
    return (1, p1) if len(p1) > 0 else (2, p2)


_, wp = game(p1, p2)
print(sum((len(wp) - i) * v for i, v in enumerate(wp)))
