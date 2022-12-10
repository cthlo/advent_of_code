import fileinput

screen = [""]
cycle = 0
x = 1


def draw():
    global screen, cycle
    screen[-1] += "#" if x - 2 < cycle < x + 2 else "."
    if len(screen[-1]) == 40:
        screen.append("")
    cycle = (cycle + 1) % 40


for line in fileinput.input():
    op, n, *_ = line.split() + [""]
    draw()
    if op == "addx":
        draw()
        x += int(n)

print("\n".join(screen))
