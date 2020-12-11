import fileinput
import re

checks = {
    "byr": lambda s: 1920 <= int(s) <= 2002,
    "iyr": lambda s: 2010 <= int(s) <= 2020,
    "eyr": lambda s: 2020 <= int(s) <= 2030,
    "hgt": lambda s: 150 <= int(s[:-2]) <= 193
    if s[-2:] == "cm"
    else 59 <= int(s[:-2]) <= 76
    if s[-2:] == "in"
    else False,
    "hcl": lambda s: re.match(r"^#[0-9a-f]{6}$", s),
    "ecl": lambda s: s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda s: re.match(r"^[0-9]{9}$", s),
}

count = 0
with fileinput.input() as f:
    while True:
        fields = dict(
            kv.split(":") for kv in " ".join(iter(lambda: next(f).strip(), "")).split()
        )
        try:
            if all(validate(fields.get(k, "")) for k, validate in checks.items()):
                count += 1
        except ValueError:
            pass

        if len(fields) == 0:
            break

print(count)
