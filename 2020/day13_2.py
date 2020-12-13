import fileinput
from functools import reduce

_, buses = list(fileinput.input())

a_s, ns = zip(
    *((-neg_a, int(n)) for neg_a, n in enumerate(buses.split(",")) if n != "x")
)


def inv(y, n):
    # https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers
    t, nt = 0, 1
    r, nr = n, y
    while nr != 0:
        q = r // nr
        t, nt = nt, t - q * nt
        r, nr = nr, r - q * nr
    return t + n if t < 0 else t


# https://brilliant.org/wiki/chinese-remainder-theorem/
N = reduce(lambda i, j: i * j, ns)
ys = [N // n for n in ns]
zs = [inv(y, n) for y, n in zip(ys, ns)]
x = sum(a * y * z for a, y, z in zip(a_s, ys, zs))

while x >= N or x < 0:
    x += (N if x < 0 else -N)

print(x)
