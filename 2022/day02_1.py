import fileinput
from typing import Literal, cast

L = Literal["A", "B", "C"]
R = Literal["X", "Y", "Z"]

shapes: dict[R, int] = {"X": 1, "Y": 2, "Z": 3}
outcomes: dict[tuple[L, R], int] = {
    ("A", "X"): 3,
    ("A", "Y"): 6,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("B", "Y"): 3,
    ("B", "Z"): 6,
    ("C", "X"): 6,
    ("C", "Y"): 0,
    ("C", "Z"): 3,
}


def score(l: L, r: R) -> int:
    return shapes[r] + outcomes[(l, r)]


print(sum(score(*cast(tuple[L, R], line.split())) for line in fileinput.input()))
