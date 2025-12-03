import itertools
import sys


def parse_input(puzzle_input):
    return (puzzle_input.splitlines(),)


def part_one(banks):
    return sum(
        max(int("".join(item)) for item in itertools.combinations(bank, 2))
        for bank in banks
    )


def part_two(banks):
    joltage = 0
    for bank in banks:
        p, on = 0, ""
        for q in range(11, -1, -1):
            d, i = max((c, -i) for i, c in enumerate(bank[p : len(bank) - q], start=p))
            p, on = (-i + 1), on + d

        joltage += int(on)

    return joltage


class Test:
    example = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 357

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 3121910778619


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
