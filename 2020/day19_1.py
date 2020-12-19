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


pat = re.compile(expand(rules[0]))
print(sum(1 for m in messages if pat.fullmatch(m)))
