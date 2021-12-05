def problem1(commands: list[tuple[str, int]]) -> int:
    cur_depth: int = 0
    cur_pos: int = 0
    for (word, value) in commands:
        if word == "forward":
            cur_pos += value
        elif word == "up":
            cur_depth -= value
        elif word == "down":
            cur_depth += value
    return cur_depth * cur_pos


def problem2(commands: list[tuple[str, int]]) -> int:
    cur_depth: int = 0
    cur_pos: int = 0
    cur_aim: int = 0
    for (word, value) in commands:
        if word == "forward":
            cur_pos += value
            cur_depth = cur_depth + (cur_aim * value)
        elif word == "up":
            cur_aim -= value
        elif word == "down":
            cur_aim += value
    return cur_depth * cur_pos
