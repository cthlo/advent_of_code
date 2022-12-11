import fileinput
import operator
from typing import Callable


class Monkey:
    items: list[int]
    op: Callable[[int], int]
    throw: Callable[[int], int]
    num_inspects: int = 0

    def __init__(
        self, items: list[int], op: tuple[str, str], test: tuple[int, int, int]
    ):
        self.items = items
        self.op = lambda x: {"*": operator.mul, "+": operator.add}[op[0]](
            x, x if op[1] == "old" else int(op[1])
        )
        self.throw = lambda x: test[1] if x % test[0] == 0 else test[2]

    def inspect(self):
        for item in self.items:
            self.num_inspects += 1
            x = self.op(item) // 3
            yield (self.throw(x), x)


monkeys = []
inp = fileinput.input()
while next(inp, None):
    monkeys.append(
        Monkey(
            [int(s) for s in next(inp).strip()[16:].split(", ")],
            tuple(next(inp).strip()[21:].split()),
            (
                int(next(inp).split()[-1]),
                int(next(inp).split()[-1]),
                int(next(inp).split()[-1]),
            ),
        )
    )
    next(inp, None)

for _ in range(20):
    for monkey in monkeys:
        for target, item in monkey.inspect():
            monkey.items = []
            monkeys[target].items.append(item)

a, b = sorted(monkey.num_inspects for monkey in monkeys)[-2:]
print(a * b)
