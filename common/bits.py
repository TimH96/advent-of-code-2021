from functools import reduce
from operator import mul


class BITSPacket:
    def __init__(self, code: str) -> None:
        # header and meta
        self.version: int = int(code[0:3], 2)
        self.type_id: int = int(code[3:6], 2)
        self.bin_len: int = 6

        # literal value parsing
        if self.type_id == 4:
            groups: list[str] = []
            while True:
                groups.append(code[self.bin_len : self.bin_len + 5])
                self.bin_len += 5
                if groups[-1][0] == "0":
                    self.literal_value: int = int("".join([x[1:] for x in groups]), 2)
                    break

        # operator parsing
        else:
            self.sub_packets: list[BITSPacket] = []

            self.len_type_id: int = int(code[self.bin_len])
            self.bin_len += 1

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
                self.sub_packets.append(pckt)
                self.bin_len += pckt.bin_len

                if (
                    len(self.sub_packets) == SUB_AMOUNT
                    or sum([x.bin_len for x in self.sub_packets]) == TOTAL_LEN
                ):
                    break

    def get_sum_of_versions(self) -> int:
        if self.type_id == 4:
            return self.version
        else:
            return self.version + sum(
                [x.get_sum_of_versions() for x in self.sub_packets]
            )

    def get_value(self) -> int:
        return int(
            {
                0: lambda: sum([x.get_value() for x in self.sub_packets]),
                1: lambda: reduce(mul, [x.get_value() for x in self.sub_packets]),
                2: lambda: min([x.get_value() for x in self.sub_packets]),
                3: lambda: max([x.get_value() for x in self.sub_packets]),
                4: lambda: self.literal_value,
                5: lambda: (
                    self.sub_packets[0].get_value() > self.sub_packets[1].get_value()
                ),
                6: lambda: (
                    self.sub_packets[0].get_value() < self.sub_packets[1].get_value()
                ),
                7: lambda: (
                    self.sub_packets[0].get_value() == self.sub_packets[1].get_value()
                ),
            }.get(self.type_id)()
        )
