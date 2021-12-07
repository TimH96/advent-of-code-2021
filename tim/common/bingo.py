class BoardEntry:
    def __init__(self, number: int, *, state: bool = False) -> None:
        self.number = number
        self.state = state


class BingoBoard:

    board: list[list[BoardEntry]]

    def __init__(self, raw: list[str], *, size: int = 5) -> None:
        self.GRID_SIZE: int = size
        self.board = self.parse_input(raw)

    def sum(self) -> int:
        """Sum of all unmarked numbers in board."""
        return sum(
            [
                sum([entry.number for entry in row if not entry.state])
                for row in self.board
            ]
        )

    def parse_input(self, raw: str) -> list[list[BoardEntry]]:
        """Parses text-formatted bingo board into proper representation."""
        return [
            [BoardEntry(int(number_str)) for number_str in row.split()]
            for row in raw.split("\n")
        ]

    def check(self, number: int) -> bool:
        """Try to check off number on a board, return True if a bingo is completed."""
        for i, row in enumerate(self.board):
            for j, entry in enumerate(row):
                if entry.number == number:
                    entry.state = True
                    if self.row_completed(i):
                        return True
                    if self.column_completed(j):
                        return True
        return False

    def row_completed(self, index: int) -> bool:
        """Check if a given row has a completed bingo."""
        return all([x.state for x in self.board[index]])

    def column_completed(self, index: int) -> bool:
        """Check if a given column has a completed bingo."""
        return all([x[index].state for x in self.board])
