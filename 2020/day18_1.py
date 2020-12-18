import fileinput


add = lambda x, y: x + y
mul = lambda x, y: x * y


def solve(it):
    result = 0
    op = add
    while (v := next(it, ")")) != ")":
        if v == "*":
            op = mul
        elif v == "+":
            op = add
        elif v == "(":
            result = op(result, solve(it))
        else:
            result = op(result, int(v))
    return result


print(
    sum(
        solve(iter(line.replace("(", "( ").replace(")", " )").split()))
        for line in fileinput.input()
    )
)
