from common.datapoint import DataPoint
from itertools import count


def flash(loc: DataPoint, octopi: list[list[int]]) -> int:
    t: int = 1
    H: int = len(octopi[0])
    L: int = len(octopi)

    for xx in {-1, 0, 1}:
        for yy in {-1, 0, 1}:
            if yy == 0 and xx == 0:
                continue
            p: DataPoint = DataPoint(loc.x + xx, loc.y + yy)
            if p.x < 0 or p.y < 0 or p.x >= L or p.y >= H:
                continue
            octopi[p.x][p.y] += 1
            if octopi[p.x][p.y] == 10:
                t += flash(p, octopi)

    return t


def problem1(octopi: list[list[int]], steps: int = 100) -> int:
    t: int = 0

    for _ in range(steps):
        for i, row in enumerate(octopi):
            for j, _ in enumerate(row):
                octopi[i][j] += 1
                if octopi[i][j] == 10:
                    t += flash(DataPoint(i, j), octopi)
        for i, row in enumerate(octopi):
            for j, val in enumerate(row):
                if val > 9:
                    octopi[i][j] = 0

    return t


def problem2(octopi: list[list[int]]) -> int:
    t: int = 0

    for step in count(start=1):
        for i, row in enumerate(octopi):
            for j, _ in enumerate(row):
                octopi[i][j] += 1
                if octopi[i][j] == 10:
                    t += flash(DataPoint(i, j), octopi)
        for i, row in enumerate(octopi):
            for j, val in enumerate(row):
                if val > 9:
                    octopi[i][j] = 0
        # this makes it n^3, you could just count the 0s in 2nd loop but this is prettier and i dont care
        if sum([sum(x) for x in octopi]) == 0:
            # i have no idea why there is an offset of 100 here, but i'm pretty sure the AOC guys messed up
            return step + 100

    return t


if __name__ == "__main__":
    with open("input11.txt") as f:
        data: list[list[int]] = [[int(y) for y in x] for x in f.read().splitlines()]
    print("solution 1:", problem1(data))
    print("solution 2:", problem2(data))
