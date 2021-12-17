if __name__ == "__main__":
    to_bin = lambda x: bin(int(x, 16)).split("b")[1].rjust(4, "0")
    with open("input16.txt") as f:
        data: str = "".join([to_bin(char) for char in f.read().splitlines()[0]])
    # print("solution 1:", problem1(data))
    # print("solution 2:", problem2(data))
