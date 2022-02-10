PAIRS: dict[str, str] = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def problem1(navigation: list[str]) -> int:
    VALUES: dict[str, int] = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    t: int = 0

    for line in navigation:
        stack: list[str] = []
        for char in line:
            if char in PAIRS.keys():
                stack.append(PAIRS[char])
            elif char == stack[-1]:
                stack.pop()
            else:
                t += VALUES[char]
                break

    return t


def problem2(navigation: list[str]) -> int:
    VALUES: dict[str, int] = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    completions: list[int] = []

    for i, line in enumerate(navigation):
        corrupt: bool = False
        stack: list[str] = []
        for char in line:
            if char in PAIRS.keys():
                stack.append(PAIRS[char])
            elif char == stack[-1]:
                stack.pop()
            else:
                corrupt = True
                break

        if not corrupt:
            t: int = 0
            for char in stack[::-1]:
                t = (t * 5) + VALUES[char]
            completions.append(t)

    completions.sort()
    return completions[round((len(completions) - 1) / 2)]


if __name__ == "__main__":
    with open("input10.txt") as f:
        data: list[str] = f.read().splitlines()
    print("solution 1:", problem1(data))
    print("solution 2:", problem2(data))
