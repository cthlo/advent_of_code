import fileinput

prios = {chr(i + 97): i + 1 for i in range(26)} | {
    chr(i + 65): i + 27 for i in range(26)
}

inp = fileinput.input()
sum = 0
for a in inp:
    b, c = set(next(inp).strip()), set(next(inp).strip())
    sum += prios[set.intersection(set(a.strip()), b, c).pop()]

print(sum)
