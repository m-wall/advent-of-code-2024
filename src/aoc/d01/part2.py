from aoc.helpers.decorators import timer


def solve(puzzle_input):
    answer = 0
    lines = puzzle_input.splitlines()

    list_a = []
    list_b = []

    for line in lines:
        a, b = line.split()
        list_a.append(int(a))
        list_b.append(int(b))

    for item_a in list_a:
        answer += item_a * list_b.count(item_a)

    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
