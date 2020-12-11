import fileinput
import re

p = re.compile(r"\d*")

h = {}
for line in fileinput.input():
    parent_color, children = line.split(" bags contain ")
    for child in children.split(", "):
        child_color = " ".join(child.split()[-3:-1])
        try:
            count = int(p.search(child).group(0))
        except ValueError:
            pass
        else:
            h.setdefault(parent_color, []).append((count, child_color))

stk = list(h["shiny gold"])
total = 0
while stk:
    count, child = stk.pop()
    total += count
    stk.extend(
        [
            (count * grandcount, grandchild)
            for grandcount, grandchild in h.get(child, [])
        ]
    )

print(total)
