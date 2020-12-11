import fileinput

nums = sorted(int(line) for line in fileinput.input())
nums.append(nums[-1] + 3)

h = {0: 1}
for n in nums:
    h[n] = h.get(n - 1, 0)
    h[n] += h.get(n - 2, 0)
    h[n] += h.get(n - 3, 0)

print(h[nums[-1]])
