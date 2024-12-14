from aoc.helpers.decorators import timer


def solve(puzzle_input):
    answer = 0
    rules_str, updates_str = puzzle_input.split("\n\n")

    rules = [x.split("|") for x in rules_str.splitlines()]
    updates = [x.split(",") for x in updates_str.splitlines()]

    for update in updates:
        for x, y in rules:
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    break
        else:
            answer += int(update[len(update) // 2])
    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
