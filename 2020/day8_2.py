import fileinput

# build graphs
lines = list(fileinput.input())
nodes = {}
for pos, line in enumerate(lines):
    op, arg = line.split()
    suc = pos + int(arg) if op == "jmp" else pos + 1

    nodes.setdefault(pos, {"from": []})["to"] = suc
    nodes.setdefault(suc, {"from": []})["from"].append(pos)

# find target graph
stk = [len(lines)]
targets = set()
while stk:
    pos = stk.pop()
    targets.add(pos)
    for pre in nodes[pos]["from"]:
        stk.append(pre)

# traverse and try fix op
pos = 0
acc = 0
while True:
    op = lines[pos][:3]
    if op == "jmp":
        if pos + 1 in targets:
            pos = pos + 1
            break
    elif op == "nop":
        if pos + int(lines[pos][3:]) in targets:
            pos = pos + int(lines[pos][3:])
            break
    else:
        acc += int(lines[pos][3:])
    pos = nodes[pos]["to"]

# complete rest of instructions
while pos != len(lines):
    op, arg = lines[pos].split()
    if op == "acc":
        acc += int(arg)
    pos = nodes[pos]["to"]

print(acc)
