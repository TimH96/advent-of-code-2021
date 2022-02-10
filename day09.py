def get_lowpoints(heightmap: list[list[int]]) -> list[tuple[int, int]]:
    H: int = len(heightmap[0])
    L: int = len(heightmap)
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


def problem2(heightmap: list[list[int]]) -> int:
    top3: list[int] = [0] * 3
    lowpoints = get_lowpoints(heightmap)
    H: int = len(heightmap[0])
    L: int = len(heightmap)
    for (startpoint_x, startpoint_y) in lowpoints:
        visited: set[tuple[int, int]] = set()
        search: set[tuple[int, int]] = {(startpoint_x, startpoint_y)}
        while len(search) > 0:
            new_search: set[tuple[int, int]] = set()
            for (i, j) in search:
                visited.add((i, j))
                for (x, y) in [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]:
                    if (
                        (x < 0 or y < 0 or x >= L or y >= H)
                        or (heightmap[x][y] == 9)
                        or ((x, y) in visited)
                    ):
                        continue
                    else:
                        new_search.add((x, y))
            search = new_search

        top3[0] = max(top3[0], len(visited))
        top3.sort()

    return top3[0] * top3[1] * top3[2]


if __name__ == "__main__":
    with open("input09.txt") as f:
        data: list[list[int]] = [[int(y) for y in x] for x in f.read().splitlines()]
    print("solution 1:", problem1(data))
    print("solution 2:", problem2(data))
