from queue import PriorityQueue
from collections import defaultdict


def problem1(risk_map: list[list[int]]) -> int:
    H: int = len(risk_map[0])
    L: int = len(risk_map)

    lowest_risk: dict[tuple[int, int], int] = defaultdict(lambda: -1)
    lowest_risk[(0, 0)] = 0

    q: PriorityQueue[tuple[int, tuple[int, int]]] = PriorityQueue()
    q.put((0, (0, 0)))

    while not q.empty():
        (_, (x, y)) = q.get()

        for (xx, yy) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if xx < 0 or yy < 0 or xx >= L or yy >= H:
                continue
            r: int = risk_map[xx][yy] + lowest_risk[(x, y)]
            if lowest_risk[(xx, yy)] == -1 or r < lowest_risk[(xx, yy)]:
                lowest_risk[(xx, yy)] = r
                q.put((r, (xx, yy)))

    return lowest_risk[(L - 1, H - 1)]


def problem2(risk_map: list[list[int]]) -> int:
    new_map: list[list[int]] = []

    for row in risk_map:
        r: list[int] = row
        for i in range(1, 5):
            r = r + [y - (9 * (y > 9)) for y in [x + i for x in row]]
        new_map.append(r)

    cop = [x for x in new_map]
    for i in range(1, 5):
        for row in cop:
            new_map.append([y - (9 * (y > 9)) for y in [x + i for x in row]])

    return problem1(new_map)


if __name__ == "__main__":
    with open("input15.txt") as f:
        data: list[list[int]] = [[int(y) for y in x] for x in f.read().splitlines()]
    print("solution 1:", problem1(data))
    print("solution 2:", problem2(data))
