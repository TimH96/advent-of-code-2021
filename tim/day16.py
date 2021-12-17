class BITSPacket:
    def __init__(self, code: str) -> None:
        CLEN: int = len(code)

        # header and meta
        self.version: int = int(code[0:3], 2)
        self.type_id: int = int(code[3:6], 2)
        self.bin_len: int = 6

        # literal value parsing
        if self.type_id == 4:
            groups: list[str] = []
            while True:
                broke: bool = False
                groups.append(code[self.bin_len : self.bin_len + 5])
                self.bin_len += 5
                if groups[-1][0] == "0":
                    while True:
                        if self.bin_len < CLEN and code[self.bin_len] == "0":
                            self.bin_len += 1
                        else:
                            broke = True
                            break
                if broke:
                    self.literal_value: int = int("".join([x[1:] for x in groups]), 2)
                    break

        # operator parsing
        else:
            self.sub_packets: list[BITSPacket] = []

            self.bin_len += 1
            self.len_type_id: int = int(code[self.bin_len])

            SUB_AMOUNT: int = -1
            TOTAL_LEN: int = -1

            # parsing based on subpacket amount
            if self.len_type_id:
                SUB_AMOUNT = int(code[self.bin_len : self.bin_len + 11], 2)
                self.bin_len += 11

            # parsing based on total length
            else:
                TOTAL_LEN = int(code[self.bin_len : self.bin_len + 15], 2)
                self.bin_len += 15

            # iteratively parse subpackets
            while True:
                pckt = BITSPacket(code[self.bin_len :])
                self.bin_len += pckt.bin_len
                self.sub_packets.append(pckt)
                if (
                    len(self.sub_packets) == SUB_AMOUNT
                    or sum([x.bin_len for x in self.sub_packets]) == TOTAL_LEN
                ):
                    break


def problem1(code: str) -> None:
    root = BITSPacket(code)
    print(root.bin_len == len(code))


if __name__ == "__main__":
    to_bin = lambda x: bin(int(x, 16)).split("b")[1].rjust(4, "0")
    with open("input16.txt") as f:
        data: str = "".join([to_bin(char) for char in f.read().splitlines()[0]])
    print("solution 1:", problem1(data))
    # print("solution 2:", problem2(data))
