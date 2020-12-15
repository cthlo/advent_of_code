import fileinput

nums = [int(i) for i in next(fileinput.input()).split(",")]

h = {n: i for i, n in enumerate(nums)}
for i in range(len(nums), 30000000):
    if h[nums[-1]] != i - 1:
        nums.append(i - 1 - h[nums[-1]])
        h[nums[i - 1]] = i - 1
    else:
        nums.append(0)
    h.setdefault(nums[-1], i)

print(nums[-1])
