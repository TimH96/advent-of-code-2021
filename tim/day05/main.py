from typing import Callable, Counter
from datapoint import DataPoint
from itertools import chain


def problem1(data: list[tuple[DataPoint, DataPoint]], grid_size: int = 1000):
    grid: list[list[int]] = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    counter: int = 0

    def add_point(x, y) -> None:
        nonlocal counter
        grid[x][y] += 1
        if grid[x][y] == 2:
            counter += 1

    # vertical
    for (p1, p2) in [pair for pair in data if pair[0].x == pair[1].x]:
        for y in range(min(p1.y, p2.y), max(p1.y, p2.y) + 1):
            add_point(p1.x, y)
    # horizontal
    for (p1, p2) in [pair for pair in data if pair[0].y == pair[1].y]:
        for x in range(min(p1.x, p2.x), max(p1.x, p2.x) + 1):
            add_point(x, p1.y)
    return counter


def problem2():
    pass


if __name__ == "__main__":
    with open("input.txt") as f:
        data: list[tuple[DataPoint, DataPoint]] = [
            (DataPoint(z[0][0], z[0][1]), DataPoint(z[1][0], z[1][1]))
            for z in [
                [y.split(",") for y in x.split(" -> ")] for x in f.read().splitlines()
            ]
        ]
    print("solution 1:", problem1(data))
    # print("solution 2:", problem2(data))
