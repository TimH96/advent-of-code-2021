def create_map(raw: list[str]) -> dict[str, set[str]]:
    this_map: dict[str, set[str]] = {}
    for (source, destination) in [line.split("-") for line in raw]:
        for (x, y) in [(source, destination), (destination, source)]:
            if x in this_map.keys():
                this_map[x].add(y)
            else:
                this_map[x] = set([y])
    return this_map


def problem1(cave_map: dict[str, set[str]]) -> int:
    def viable_paths(point: str, visited: list[str]) -> list[list[str]]:
        if (point[0].islower() and point in visited) or (point == "end"):
            return [[point]]
        else:
            out: list[list[str]] = []
            new_v: list[str] = visited + [point]
            for dest in cave_map[point]:
                for path in viable_paths(dest, new_v):
                    out.append([point] + path)
            return out

    return len([path for path in viable_paths("start", []) if path[-1] == "end"])


def problem2(cave_map: dict[str, set[str]]) -> int:
    def viable_paths(
        point: str, visited: list[str], double_cave: str
    ) -> list[list[str]]:
        if point == "end":
            return [[point]]  # exit path
        if point[0].islower():
            if point in visited:
                if double_cave or point == "start":
                    return [[point]]  # exit path
                else:
                    double_cave = point
        out: list[list[str]] = []
        new_v: list[str] = visited + [point]
        for dest in cave_map[point]:
            for path in viable_paths(dest, new_v, double_cave):
                out.append([point] + path)
        return out

    return len([path for path in viable_paths("start", [], "") if path[-1] == "end"])


if __name__ == "__main__":
    with open("input12.txt") as f:
        data: dict[str, set[str]] = create_map(f.read().splitlines())
    print("solution 1:", problem1(data))
    print("solution 2:", problem2(data))
