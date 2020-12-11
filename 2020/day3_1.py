import fileinput

x = 0
count = 0
for line in fileinput.input():
    if line[x] == "#":
        count += 1
    x = (x + 3) % len(line.strip())

print(count)
