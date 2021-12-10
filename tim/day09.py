def problem1(heightmap: list[list[int]]) -> int:
    t: int = 0
    L: int = len(heightmap[0])
    H: int = len(heightmap)
    for i, row in enumerate(heightmap):
        for j, height in enumerate(row):
            smallest: bool = True
            for (x, y) in [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]:
                if x < 0 or y < 0 or x >= L or y >= H:
                    continue
                smallest = min(smallest, height < heightmap[x][y])
            if smallest:
                t = t + 1 + heightmap[i][j]
    return t


if __name__ == "__main__":
    with open("input09.txt") as f:
        data: list[list[int]] = [[int(y) for y in x] for x in f.read().splitlines()]
    print("solution 1:", problem1(data))
