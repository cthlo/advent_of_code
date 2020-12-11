import fileinput

nums = [int(line) for line in fileinput.input()]
numset = set(nums)
for i, n in enumerate(nums):
    for j, m in enumerate(reversed(nums)):
        if 2020 - n - m in numset:
            print(n * m * (2020 - n - m))
            break
    else:
        continue
    break
