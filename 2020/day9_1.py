import fileinput

nums = [int(line) for line in fileinput.input()]
s = set(nums[:25])
for i, n in enumerate(nums[25:]):
    if all(n - m not in s for m in s):
        print(n)
        break
    s.remove(nums[i])  # assume no repeat
    s.add(n)
