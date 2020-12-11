import fileinput

required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

count = 0
with fileinput.input() as f:
    while True:
        fields = {
            kv.split(":")[0]
            for kv in " ".join(iter(lambda: next(f).strip(), "")).split()
        }
        if required.issubset(fields):
            count += 1

        if len(fields) == 0:
            break

print(count)
