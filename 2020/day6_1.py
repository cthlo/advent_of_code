import fileinput

total = 0
with fileinput.input() as f:
    while True:
        num_qs = len(set("".join(iter(lambda: next(f).strip(), ""))))
        total += num_qs

        if num_qs == 0:
            break

print(total)
