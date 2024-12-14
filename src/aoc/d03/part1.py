import re

from aoc.helpers.decorators import timer


def find_mul_strings(data):
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, data)
    return matches


def solve(puzzle_input):
    answer = 0
    muls = find_mul_strings(puzzle_input)

    for mul in muls:
        comma_digits = mul[4:-1]
        a, b = comma_digits.split(",")
        answer += int(a) * int(b)
    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()