import fileinput

sum = 0
for line in fileinput.input():
    l1, l2, r1, r2 = [int(s) for s in line.replace("-", ",").split(",")]
    sum += int((l1 <= r1 and l2 >= r2) or (l1 >= r1 and l2 <= r2))

print(sum)
