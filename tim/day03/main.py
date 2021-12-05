def problem1(diagnostic_report: list[str]) -> int:
    input_length = len(diagnostic_report[0])
    count0: list = [0] * input_length
    count1: list = [0] * input_length
    for reading in diagnostic_report:
        for i, bit in enumerate([int(x) for x in reading]):
            if bit:
                count1[i] = count1[i] + 1
            else:
                count0[i] = count0[i] + 1
    results: list = []
    for c0, c1 in zip(count0, count1):
        results.append(int(c0 < c1))
    gamma: int = 0
    epsilon: int = 0
    for i, bit in enumerate(results[::-1]):
        gamma = gamma + (2 ** i * bit)
        epsilon = epsilon + (2 ** i * int(not bit))
    return gamma * epsilon


def problem2(diagnostic_report: list[str]) -> int:
    sol: list = [0] * 2
    for k, evaluation_function in enumerate(
        [lambda x, y: int(x <= y), lambda x, y: int(x > y)]
    ):
        remaining = diagnostic_report[::]
        for i, _ in enumerate(diagnostic_report[0]):
            c0: int = len([x for x in remaining if int(x[i]) == 0])
            c1: int = len(remaining) - c0
            desired_bit = evaluation_function(c0, c1)
            remaining = [x for x in remaining if int(x[i]) == desired_bit]
            if len(remaining) == 1:
                sol[k] = int(remaining[0], 2)
                break
    return sol[0] * sol[1]
