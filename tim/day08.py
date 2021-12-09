def problem1(signals: list[tuple[str, str]]) -> int:
    t: int = 0
    for signal in signals:
        o: list[str] = signal[1].split()
        t += len([x for x in o if len(x) in [2, 3, 4, 7]])
    return t


if __name__ == "__main__":
    with open("input08.txt") as f:
        data: list[tuple[str, str]] = [
            tuple(x.split(" | ")) for x in f.read().splitlines()
        ]
    print("solution 1:", problem1(data))
    #print("solution 2:", problem2(data))
