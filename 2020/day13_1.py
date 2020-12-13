import fileinput
from math import ceil

t, buses = list(fileinput.input())
t = int(t)
ids = [int(i) for i in buses.split(",") if i != "x"]

a, b = min((ceil(t / i) * i, i) for i in ids)
print(b * (a - t))
