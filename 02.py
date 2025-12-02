import itertools
import math
import sys


def parse_input(puzzle_input):
    id_ranges = []
    for raw_id_range in puzzle_input.strip().split(","):
        fst_id, last_id = raw_id_range.split("-")
        id_ranges.append(range(int(fst_id), int(last_id) + 1))

    return (id_ranges,)


def part_one(id_ranges):
    def f(x):
        n = int(math.log10(x)) + 1
        if n % 2:
            return False

        p, q = divmod(x, 10 ** (n / 2))
        return p == q

    return sum(v for id_range in id_ranges for v in id_range if f(v))


def part_two(id_ranges):
    invalid = set(
        int("".join(item * a))
        for a, b in [
            (2, 1),
            (3, 1),
            (4, 1),
            (5, 1),
            (6, 1),
            (7, 1),
            (8, 1),
            (9, 1),
            (10, 1),
            (2, 2),
            (3, 2),
            (4, 2),
            (5, 2),
            (2, 3),
            (3, 3),
            (2, 4),
            (2, 5),
        ]
        for item in itertools.product("0123456789", repeat=b)
        if item[0] != "0"
    )

    return sum(sum(invalid & set(id_range)) for id_range in id_ranges)


class Test:
    example = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 1227775554

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 4174379265


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
