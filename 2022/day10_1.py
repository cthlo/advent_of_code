import fileinput

x = 1
cycle = 1
sum = 0


def inc():
    global cycle, sum
    cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        sum += x * cycle


for line in fileinput.input():
    op, n, *_ = line.split() + [""]
    inc()
    if op == "addx":
        x += int(n)
        inc()

print(sum)
