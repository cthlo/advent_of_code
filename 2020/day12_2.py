import fileinput

instructions = [line.strip() for line in fileinput.input()]

wp = [10, 1]
pos = [0, 0]


def clockwise():
    wp[0], wp[1] = wp[1], -wp[0]


for ins in instructions:
    act = ins[0]
    val = int(ins[1:])
    if act == "R":
        [clockwise() for _ in range(val // 90)]
    if act == "L":
        [clockwise() for _ in range(4 - val // 90)]
    if act == "F":
        pos = [pos[0] + wp[0] * val, pos[1] + wp[1] * val]
    if act == "N":
        wp[0], wp[1] = wp[0], wp[1] + val
    if act == "S":
        wp[0], wp[1] = wp[0], wp[1] - val
    if act == "E":
        wp[0], wp[1] = wp[0] + val, wp[1]
    if act == "W":
        wp[0], wp[1] = wp[0] - val, wp[1]

print(abs(pos[0]) + abs(pos[1]))
