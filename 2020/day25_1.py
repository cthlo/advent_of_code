import fileinput


def bf(pk):
    c = v = 1
    while (v := v * 7 % 20201227) != pk:
        c += 1
    return c


def transform(s, l):
    v = 1
    for _ in range(l):
        v = v * s % 20201227
    return v


with fileinput.input() as f:
    cpk = int(next(f))
    dpk = int(next(f))

    cl = bf(cpk)
    dl = bf(dpk)

    print(transform(cpk, dl))
