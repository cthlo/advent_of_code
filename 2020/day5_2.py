import fileinput

ids = [
    int(line[:7].replace("F", "0").replace("B", "1"), 2) * 8
    + int(line[7:].replace("L", "0").replace("R", "1"), 2)
    for line in fileinput.input()
]

print(((min(ids) + max(ids)) * (len(ids) + 1)) // 2 - sum(ids))
