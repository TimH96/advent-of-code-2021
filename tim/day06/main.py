from collections import deque


def problem1(swarm: list[int], iterations: int) -> int:
    # this solution is O(n*k) in time and something truly ungodly in space complexity
    # you could just replace problem1 with problem2 solution entirely, i'm keeping it here to own up to it
    sol: list[int] = [x for x in swarm]  # copy because python is funny :))))
    for _ in range(iterations):
        for i in range(len(sol)):
            if sol[i] == 0:
                sol.append(8)
                sol[i] = 6
            else:
                sol[i] -= 1
    return len(sol)


def problem2(swarm: list[int], iterations: int) -> int:
    fishes: deque[int] = deque([0] * 9)
    for fish in swarm:
        fishes[fish] += 1
    for _ in range(iterations):
        fishes[7] += fishes[0]
        fishes.rotate(-1)
    return sum(fishes)


if __name__ == "__main__":
    with open("input.txt") as f:
        data: list[int] = [int(x) for x in f.read().split(",")]
    print("solution 1:", problem1(data, 80))
    print("solution 2:", problem2(data, 256))
