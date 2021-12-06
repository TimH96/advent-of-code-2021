def problem1(swarm: list[int], iterations: int) -> int:
    sol: list[int] = swarm
    for _ in range(iterations):
        for i in range(len(sol)):
            if sol[i] == 0:
                sol.append(8)
                sol[i] = 6
            else:
                sol[i] -= 1
    return len(sol)


if __name__ == "__main__":
    with open("input.txt") as f:
        data: list[int] = [int(x) for x in f.read().split(",")]
    print("solution 1:", problem1(data, 80))
    # print("solution 2:", problem2(data))
