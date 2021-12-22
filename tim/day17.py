from itertools import count


def shoot_probe(
    target: tuple[tuple[int, int], tuple[int, int]], velocity: tuple[int, int]
) -> bool:
    vel_x, vel_y = velocity
    pos_x, pos_y = (0, 0)
    TAR_X = range(target[0][0], target[0][1] + 1)
    TAR_Y = range(target[1][0], target[1][1] + 1)
    has_reached_apex: bool = False

    while True:
        new_x, new_y = (vel_x + pos_x, vel_y + pos_y)
        if not has_reached_apex and new_y < pos_y:
            has_reached_apex = True
        pos_x, pos_y = (new_x, new_y)
        vel_x = max(0, vel_x - 1)
        vel_y -= 1

        if pos_x in TAR_X and pos_y in TAR_Y:
            return True
        if has_reached_apex and pos_y < TAR_Y[0]:
            return False


def problem1(
    target: tuple[tuple[int, int], tuple[int, int]], y_search_radius: int = 200
) -> int:
    nth_triangle = lambda x: round((x ** 2 + x) / 2)

    # assuming target area with positive x
    mx: int = 0
    for x in count(0):
        if nth_triangle(x) > target[0][1]:
            mx = x
            break

    my: int = 0
    # just searching for n amount of y values seems a bit bruteforce here but i couldn't find
    # a particular pretty exit criteria either. maybe something like finding the y value which
    # guarantees that gravity will lead to skipping over the target area aka:
    #   my = y where gravity at highest point of TARGET_Y is size(TARGET_Y)*2
    for y in range(y_search_radius):
        for x in range(mx):
            if shoot_probe(target, (x, y)):
                my = y
                break

    return nth_triangle(my)


def problem2(
    target: tuple[tuple[int, int], tuple[int, int]], y_search_radius: int = 200
) -> int:
    nth_triangle = lambda x: round((x ** 2 + x) / 2)

    # assuming target area with positive x
    mx: int = 0
    for x in count(0):
        if nth_triangle(x) > target[0][1]:
            mx = x
            break

    t: int = 0
    # see problem1 for note about cringe exit criteria here
    for y in range(target[1][0], y_search_radius):
        for x in range(0, target[0][1] + 1):
            if shoot_probe(target, (x, y)):
                t += 1

    return t


if __name__ == "__main__":
    with open("input17.txt") as f:
        data: tuple[tuple[int, int], tuple[int, int]] = tuple(
            [
                (int(y[0]), int(y[1]))
                for y in [x[2:].split("..") for x in f.read()[13:].split(", ")]
            ]
        )
    print("solution 1:", problem1(data))
    print("solution 2:", problem2(data))
