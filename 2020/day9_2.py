import fileinput
from itertools import combinations

nums = [int(line) for line in fileinput.input()]
s = set(nums[:25])
for i, n in enumerate(nums[25:]):
    if all(n - m not in s for m in s):
        break
    s.remove(nums[i])  # assume no repeat
    s.add(n)

i = 0
j = 1
s = nums[0]
while True:
    if s == n:
        print(max(nums[i:j]) + min(nums[i:j]))
        break
    elif s < n:
        s += nums[j]
        j += 1
    else:
        s -= nums[i]
        i += 1
