import fileinput

h = {}
for line in fileinput.input():
    child_color, parents = line.split(" bags contain ")
    for parent in parents.split(", "):
        parent_color = " ".join(parent.split()[-3:-1])
        h.setdefault(parent_color, []).append(child_color)

visited = set()
stk = list(h["shiny gold"])
count = 0
while stk:
    child = stk.pop()
    if child not in visited:
        visited.add(child)
        stk.extend(h.get(child, []))

print(len(visited))
