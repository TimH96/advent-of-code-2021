from dataclasses import dataclass


@dataclass(frozen=True)
class DataPoint:

    x: int
    y: int

    def __post_init__(self):
        """Convert given value to int."""
        if not isinstance(self.x, int):
            self.x = int(self.x)
        if not isinstance(self.y, int):
            self.y = int(self.y)
