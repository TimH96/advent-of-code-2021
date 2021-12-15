from collections import defaultdict


def problem1(template: str, rules: dict[str, str], iterations: int = 10) -> int:
    new: list[str] = list(template)

    for _ in range(iterations):
        cur = new
        new = []
        for i, _ in enumerate(cur):
            new.append(cur[i])
            try:
                pair: str = cur[i] + cur[i + 1]
            except IndexError:
                break
            if pair in rules.keys():
                new.append(rules[pair])

    occurences: dict[str, int] = defaultdict(lambda: 0)
    for letter in set(new):
        occurences[letter] = new.count(letter)

    return max(occurences.values()) - min(occurences.values())


def problem2(template: str, rules: dict[str, str], iterations: int = 40) -> int:
    quantity: dict[str, int] = defaultdict(lambda: 0)

    for i, _ in enumerate(template):
        try:
            quantity[template[i] + template[i + 1]] += 1
        except IndexError:
            break

    for _ in range(iterations):
        for (pair, val) in [(x, y) for (x, y) in quantity.items() if y > 0]:
            if pair in rules.keys():
                c: str = rules[pair]
                quantity[pair] -= val
                quantity[pair[0] + c] += val
                quantity[c + pair[1]] += val

    occurences: dict[str, int] = defaultdict(lambda: 0)
    for ((letter1, letter2), value) in list(quantity.items()) + [
        ((template[0], template[-1]), 1)
    ]:
        occurences[letter1] += value
        occurences[letter2] += value
    occurences = {x: round(y / 2) for (x, y) in occurences.items()}

    return max(occurences.values()) - min(occurences.values())


if __name__ == "__main__":
    with open("input14.txt") as f:
        (template, raw_rules) = f.read().split("\n\n")
        rules: dict[str, str] = {
            y[0]: y[1] for y in [tuple(x.split(" -> ")) for x in raw_rules.splitlines()]
        }
    print("solution 1:", problem1(template, rules, 10))
    print("solution 2:", problem2(template, rules, 40))
