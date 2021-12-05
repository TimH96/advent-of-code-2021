from bingo import BingoBoard


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
