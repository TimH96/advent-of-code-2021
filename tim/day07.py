def problem1(crabs: list[int]) -> int:
    def used_fuel_for_position(desired_position: int) -> int:
        return sum([abs(crab - desired_position) for crab in crabs])

    return min([used_fuel_for_position(i) for i, _ in enumerate(crabs)])


def problem2(crabs: list[int]) -> int:
    def used_fuel_for_position(desired_position: int) -> int:
        return sum(
            [
                # formula taken from here: https://math.stackexchange.com/a/593320
                round(
                    (abs(crab - desired_position) ** 2 + abs(crab - desired_position))
                    / 2
                )
                for crab in crabs
            ]
        )

    return min([used_fuel_for_position(i) for i, _ in enumerate(crabs)])


if __name__ == "__main__":
    with open("input07.txt") as f:
        data: list[int] = [int(x) for x in f.read().split(",")]
    print("solution 1:", problem1(data))
    print("solution 2:", problem2(data))
