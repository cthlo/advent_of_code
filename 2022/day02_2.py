import fileinput
from typing import Literal, cast

L = Literal["A", "B", "C"]
R = Literal["X", "Y", "Z"]

outcomes: dict[R, int] = {"X": 0, "Y": 3, "Z": 6}
plays: dict[tuple[L, R], int] = {
    ("A", "X"): 3,
    ("A", "Y"): 1,
    ("A", "Z"): 2,
    ("B", "X"): 1,
    ("B", "Y"): 2,
    ("B", "Z"): 3,
    ("C", "X"): 2,
    ("C", "Y"): 3,
    ("C", "Z"): 1,
}


def score(l: L, r: R) -> int:
    return outcomes[r] + plays[(l, r)]


print(sum(score(*cast(tuple[L, R], line.split())) for line in fileinput.input()))
