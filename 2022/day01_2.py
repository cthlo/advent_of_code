import fileinput
from heapq import nlargest
from typing import Generator


def cals() -> Generator[int, None, None]:
    cal = 0
    for line in fileinput.input():
        if line == "\n":
            yield cal
            cal = 0
        else:
            cal += int(line)


print(sum(nlargest(3, cals())))
