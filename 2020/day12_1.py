import fileinput

instructions = [line.strip() for line in fileinput.input()]

dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]

face = 0
pos = [0, 0]
for ins in instructions:
    act = ins[0]
    val = int(ins[1:])
    if act == "R":
        face = (face + val // 90) % 4
    if act == "L":
        face = (face - val // 90) % 4
    if act == "F":
        pos = [pos[0] + dirs[face][0] * val, pos[1] + dirs[face][1] * val]
    if act == "N":
        pos = [pos[0], pos[1] + val]
    if act == "S":
        pos = [pos[0], pos[1] - val]
    if act == "E":
        pos = [pos[0] + val, pos[1]]
    if act == "W":
        pos = [pos[0] - val, pos[1]]

print(abs(pos[0]) + abs(pos[1]))
