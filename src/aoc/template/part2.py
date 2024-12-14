from aoc.helpers.decorators import timer


def solve(puzzle_input):
    answer = 0
    lines = puzzle_input.splitlines()

    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
