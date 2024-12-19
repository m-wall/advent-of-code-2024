from functools import cache

from aoc.helpers.decorators import timer


def solve(puzzle_input):
    answer = 0
    towels, designs = puzzle_input.split("\n\n")
    towels = set(towels.split(", "))
    designs = designs.strip().split("\n")

    max_towel_length = len(max(towels, key=len))

    @cache
    def towel_combinations(design):
        if design == "":
            return 1

        i, combinations = 0, 0
        while i <= len(design) and i <= max_towel_length:
            design_slice = design[:i]
            if design_slice in towels:
                combinations += towel_combinations(design[i:])
            i += 1
        return combinations

    for design in designs:
        answer += towel_combinations(design)
    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
