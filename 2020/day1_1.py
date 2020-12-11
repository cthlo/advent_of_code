import fileinput

nums = {int(line) for line in fileinput.input()}
for n in nums:
    if 2020 - n in nums:
        print((2020 - n) * n)
        break
