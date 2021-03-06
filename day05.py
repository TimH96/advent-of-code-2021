from typing import Callable
from common.datapoint import DataPoint


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


def problem2(data: list[tuple[DataPoint, DataPoint]], grid_size: int = 1000):
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
    # diagonal
    for (p1, p2) in [
        pair
        for pair in data
        if abs(pair[0].y - pair[1].y) == abs(pair[0].x - pair[1].x)
    ]:
        start: DataPoint = min([p1, p2], key=lambda p: p.x)
        stop: DataPoint = max([p1, p2], key=lambda p: p.x)
        direction_function: Callable = (
            (lambda y, step: y + step)
            if start.y < stop.y
            else (lambda y, step: y - step)
        )
        for i, x in enumerate(range(start.x, stop.x + 1)):
            add_point(x, direction_function(start.y, i))
    return counter


if __name__ == "__main__":
    with open("input05.txt") as f:
        data: list[tuple[DataPoint, DataPoint]] = [
            (DataPoint(z[0][0], z[0][1]), DataPoint(z[1][0], z[1][1]))
            for z in [
                [y.split(",") for y in x.split(" -> ")] for x in f.read().splitlines()
            ]
        ]
    print("solution 1:", problem1(data))
    print("solution 2:", problem2(data))
