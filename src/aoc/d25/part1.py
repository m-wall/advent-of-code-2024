from aoc.helpers.decorators import timer

LOCK_HEIGHT = 5


def schematic_to_numeric(strings):
    shape = []
    for col in range(len(strings[0])):
        rotated_string = "".join([row[col] for row in strings])
        shape.append(rotated_string.count("#") - 1)
    return shape


def solve(puzzle_input):
    answer = 0
    schematic_blocks = puzzle_input.split("\n\n")

    locks = []
    keys = []

    for schematic_block in schematic_blocks:
        lines = schematic_block.strip().split("\n")
        if all(char == "#" for char in lines[0]):
            locks.append(schematic_to_numeric(lines))
        else:
            keys.append(schematic_to_numeric(lines))

    for lock in locks:
        for key in keys:
            if all(l_val + k_val <= LOCK_HEIGHT for l_val, k_val in zip(lock, key)):
                answer += 1

    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
