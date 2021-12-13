def fold(
    points: set[tuple[int, int]], instructions: list[tuple[str, int]]
) -> set[tuple[int, int]]:
    if not instructions:
        return points

    this_inst = instructions.pop(0)
    dim: int = 0 if this_inst[0] == "x" else 1
    fline: int = this_inst[1]
    new_points = {p for p in points if p[dim] < fline}
    for point in {p for p in points if p[dim] > fline}:
        coord: int = fline - (point[dim] - fline)
        new_p: tuple[int, int] = (point[0], coord) if dim else (coord, point[1])
        new_points.add(new_p)

    return fold(new_points, instructions)


def problem1(points: set[tuple[int, int]], instructions: list[tuple[str, int]]) -> int:
    return len(fold(points, instructions[:1]))


def problem2(points: set[tuple[int, int]], instructions: list[tuple[str, int]]) -> str:
    final = fold(points, instructions)
    out: list[str] = ["\n"]
    for y in range(max(final, key=lambda p: p[1])[1] + 1):
        for x in range(max(final, key=lambda p: p[0])[0] + 1):
            ele: str = "#" if (x, y) in final else " "
            out.append(ele)
        out.append("\n")
    return "".join(out)


if __name__ == "__main__":
    with open("input13.txt") as f:
        (raw_points, raw_instructions) = f.read().split("\n\n")
        points: set[tuple[int, int]] = [
            (int(y[0]), int(y[1]))
            for y in [x.split(",") for x in raw_points.splitlines()]
        ]
        inst: list[tuple[str, int]] = [
            (y[0], int(y[1]))
            for y in [x[11:].split("=") for x in raw_instructions.splitlines()]
        ]
    print("solution 1:", problem1(points, inst))
    print("solution 2:", problem2(points, inst))
