def problem1(scannings: list[int]) -> int:
    sol: int = 0
    cur: int = scannings[0]
    for scan in scannings[1:]:
        if scan > cur:
            sol += 1
        cur = scan
    return sol


def problem2(scannings: list[int]) -> int:
    sol: int = 0
    cur: int = sum(scannings[0:3])
    for i, _ in enumerate(scannings[1:]):
        if len(scannings[i:]) < 3:
            break
        s: int = sum(scannings[i : i + 3])
        if s > cur:
            sol += 1
        cur = s
    return sol


if __name__ == "__main__":
    pass
