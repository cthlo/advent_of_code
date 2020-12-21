import fileinput
from functools import reduce
from itertools import permutations

alle = {}
ingr = []
food = []
with fileinput.input() as f:
    for line in f:
        lhs, rhs = line[:-2].split(" (contains ")
        ii = lhs.split()
        aa = rhs.split(", ")
        food.append((ii, aa))
        ingr.extend(ii)
        for a in aa:
            alle.setdefault(a, []).append(set(ii))

alle_ingr = sorted(
    reduce(set.union, (reduce(set.intersection, ii) for a, ii in alle.items()))
)

alle_food = [([i for i in ii if i in alle_ingr], aa) for ii, aa in food]

alle = sorted(alle)

eqs = []
for ii, aa in alle_food:
    lhs = [1 if i in ii else 0 for i in alle_ingr]
    rhs = [1 if a in aa else 0 for a in alle]
    eqs.append((lhs, rhs))

for cc in permutations(range(len(alle_ingr)), len(alle)):
    if all(all(lhs[c] >= r for c, r in zip(cc, rhs)) for lhs, rhs in eqs):
        print(",".join(alle_ingr[c] for c in cc))
