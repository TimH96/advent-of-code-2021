def problem1(signals: list[tuple[str, str]]) -> int:
    t: int = 0
    for signal in signals:
        o: list[str] = signal[1].split()
        t += len([x for x in o if len(x) in [2, 3, 4, 7]])
    return t


def problem2(signals: list[tuple[str, str]]) -> int:
    t: int = 0

    for raw_signal in signals:
        numbers: dict[int, set[str]] = {}
        i: list[str] = raw_signal[0].split()
        o: list[str] = raw_signal[1].split()

        # find the unique length numbers
        for (n, leng) in [(1, 2), (4, 4), (7, 3), (8, 7)]:
            numbers[n] = set([x for x in i if len(x) == leng][0])

        # find numbers of leng5 and leng6
        # both follow the same logic of comparing difference in segments between num1 and num4
        for (leng, n1, n2, n3) in [(6, 9, 0, 6), (5, 5, 2, 3)]:
            for num in [set(x) for x in i if len(x) == leng]:
                if len(num - numbers[1]) == 4:
                    if len(num - numbers[4]) == 2:
                        numbers[n1] = num
                    else:
                        numbers[n2] = num
                else:
                    numbers[n3] = num

        # calculate output of this signal
        # you could definitely make this less time complex but at point i dont care
        this_sum: int = 0
        for i, raw_o_pattern in enumerate(o[::-1]):
            o_pattern = set(raw_o_pattern)
            for (num, pattern) in numbers.items():
                if o_pattern == pattern:
                    this_sum = round(this_sum + (10 ** i * num))
        t += this_sum

    return t


if __name__ == "__main__":
    with open("input08.txt") as f:
        data: list[tuple[str, str]] = [
            tuple(x.split(" | ")) for x in f.read().splitlines()
        ]
    print("solution 1:", problem1(data))
    print("solution 2:", problem2(data))
