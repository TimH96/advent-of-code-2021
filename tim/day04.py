from common.bingo import BingoBoard


def problem1(numbers: list[int], raw_boards: list[str]) -> int:
    boards: list[BingoBoard] = [BingoBoard(x) for x in raw_boards]
    for number in numbers:
        for board in boards:
            if board.check(number):
                return number * board.sum()


def problem2(numbers: list[int], raw_boards: list[str]) -> int:
    boards: list[BingoBoard] = [BingoBoard(x) for x in raw_boards]
    latest_solution: int = 0
    for number in numbers:
        for board in boards:
            if board.check(number):
                boards = [x for x in boards if x is not board]
                latest_solution = number * board.sum()
    return latest_solution


if __name__ == "__main__":
    with open("input04.txt") as f:
        raw = f.read().split("\n\n")
        numbers: list[int] = [int(x) for x in raw[0].split(",")]
        raw_boards: list[str] = raw[1:]
    print("solution 1:", problem1(numbers, raw_boards))
    print("solution 2:", problem2(numbers, raw_boards))
