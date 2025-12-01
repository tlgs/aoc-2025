import sys


def parse_input(puzzle_input):
    rotations = []
    for line in puzzle_input.splitlines():
        match line[0]:
            case "R":
                rotations.append(int(line[1:]))
            case "L":
                rotations.append(-int(line[1:]))
            case _:
                raise ValueError

    return (rotations,)


def part_one(rotations):
    curr, total = 50, 0
    for n in rotations:
        curr = (curr + n) % 100
        total += curr == 0

    return total


def part_two(rotations):
    curr, total = 50, 0
    for n in rotations:
        sign = (-1) ** (n < 0)
        for _ in range(abs(n)):
            curr = (curr + sign) % 100
            total += curr == 0

    return total


class Test:
    example = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 3

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 6


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
