import fileinput
from functools import reduce

alle = {}
ingr = []
with fileinput.input() as f:
    for line in f:
        lhs, rhs = line[:-2].split(" (contains ")
        ii = lhs.split()
        ingr.extend(ii)
        for a in rhs.split(", "):
            alle.setdefault(a, []).append(set(ii))

alle_ingr = reduce(
    set.union, (reduce(set.intersection, ingr) for a, ingr in alle.items())
)
print(len([i for i in ingr if i not in alle_ingr]))
