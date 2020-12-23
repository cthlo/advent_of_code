import fileinput
from collections import namedtuple
from itertools import chain

nums = list(int(i) for i in next(fileinput.input()).strip())
cap = 1000000

lookup = [None] * (cap + 1)


class Cup:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt
        lookup[val] = self

    def nxt_3(self):
        return [self.nxt.val, self.nxt.nxt.val, self.nxt.nxt.nxt.val]


def move(curr):
    three = curr.nxt_3()

    # find dest
    dest = curr.val
    while (dest := dest - 1 if dest > 1 else cap) in three:
        pass

    # move three cups
    curr.nxt = lookup[three[2]].nxt
    lookup[dest].nxt, lookup[three[2]].nxt = lookup[three[0]], lookup[dest].nxt
    return curr.nxt


# build cups
curr = prev = Cup(nums[0])
for v in chain(nums[1:], range(len(nums) + 1, cap + 1)):
    cup = Cup(v)
    prev.nxt = cup
    prev = cup
prev.nxt = curr  # wrap around

for _ in range(10000000):
    curr = move(curr)

print(lookup[1].nxt.val * lookup[1].nxt.nxt.val)
