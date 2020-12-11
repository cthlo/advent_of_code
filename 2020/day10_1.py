import fileinput

nums = [0] + sorted(int(line) for line in fileinput.input())
h = {1: 0, 2: 0, 3: 1}
for i, n in enumerate(nums[1:]):
    h[nums[i + 1] - nums[i]] += 1

print(h[1] * h[3])
