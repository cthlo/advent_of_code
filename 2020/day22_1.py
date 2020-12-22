import fileinput

with fileinput.input() as f:
    next(f)
    p1 = list(int(v) for v in iter(lambda: next(f).strip(), ""))
    next(f)
    p2 = list(int(v) for v in iter(lambda: next(f).strip(), ""))

while len(p1) > 0 and len(p2) > 0:
    if p1[0] > p2[0]:
        p1.extend([p1[0], p2[0]])
    else:
        p2.extend([p2[0], p1[0]])
    p1 = p1[1:]
    p2 = p2[1:]

wp = p1 + p2
print(sum((len(wp) - i) * v for i, v in enumerate(wp)))
