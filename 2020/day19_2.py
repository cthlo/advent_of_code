import fileinput
import re

with fileinput.input() as f:
    rules = {}
    for line in iter(lambda: next(f).strip(), ""):
        lhs, rhs = line.split(": ")
        rules[int(lhs)] = [[eval(v) for v in rule.split()] for rule in rhs.split("|")]

    messages = [line.strip() for line in list(f)]


def expand(rule):
    if isinstance(rule[0], str):
        return rule[0]
    elif isinstance(rule[0], list):
        v = "|".join(expand(r) for r in rule)
        return f"({v})"
    elif isinstance(rule[0], int):
        return "".join(expand(rules[r]) for r in rule)


r42 = expand(rules[42])
r31 = expand(rules[31])

r8 = f"({r42})+"
r11 = f"({'|'.join(f'{r42}{{{i}}}{r31}{{{i}}}' for i in range(1, 5))})"  # expand rule 11 up to 5 repeats
pat = re.compile(r8 + r11)

print(sum(1 for m in messages if pat.fullmatch(m)))
