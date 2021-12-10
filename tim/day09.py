def get_lowpoints(heightmap: list[list[int]]) -> list[tuple[int, int]]:
    t: int = 0
    L: int = len(heightmap[0])
    H: int = len(heightmap)
    lowpoints: list[int] = []
    for i, row in enumerate(heightmap):
        for j, height in enumerate(row):
            smallest: bool = True
            for (x, y) in [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]:
                if x < 0 or y < 0 or x >= L or y >= H:
                    continue
                smallest = min(smallest, height < heightmap[x][y])
            if smallest:
                lowpoints.append((i, j))
    return lowpoints


def problem1(heightmap: list[list[int]]) -> int:
    t = get_lowpoints(heightmap)
    return len(t) + sum([heightmap[x][y] for (x, y) in t])


if __name__ == "__main__":
    with open("input09.txt") as f:
        data: list[list[int]] = [[int(y) for y in x] for x in f.read().splitlines()]
    print("solution 1:", problem1(data))
