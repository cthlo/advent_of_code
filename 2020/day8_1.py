import fileinput

lines = list(fileinput.input())
visited = set()
pos = 0
acc = 0
while pos not in visited:
    visited.add(pos)
    op, arg = lines[pos].split()
    if op == "acc":
        acc += int(arg)
        pos += 1
    elif op == "jmp":
        pos += int(arg)
    else:
        pos += 1

print(acc)
