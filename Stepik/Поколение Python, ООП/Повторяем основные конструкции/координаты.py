from sys import stdin
from re import search


for line in stdin:
    nums = search(r"\((-?\d+\.?\d*),\s-?(\d+\.?\d*)\)", line)
    x, y = map(float, nums.groups())

    if abs(x) <= 90 and abs(y) <= 180:
        print(True)
    else:
        print(False)
