import fileinput


def solve(it):
    result = 0
    while (v := next(it, ")")) != ")":
        if v == "*":
            return result * solve(it)
        elif v == "+":
            pass
        elif v == "(":
            result = result + solve(it)
        else:
            result = result + int(v)
    return result


print(
    sum(
        solve(iter(line.replace("(", "( ").replace(")", " )").split()))
        for line in fileinput.input()
    )
)
