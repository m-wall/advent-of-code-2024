from aoc.helpers.decorators import timer


def solve(puzzle_input):
    answer = 0
    puzzle_input = puzzle_input.strip()

    if len(puzzle_input) % 2 != 0:
        puzzle_input += "0"

    pairs = [(puzzle_input[i], puzzle_input[i + 1]) for i in range(0, len(puzzle_input), 2)]

    disk_map = []

    for i, pair in enumerate(pairs):
        file_blocks, space_blocks = pair
        disk_map.extend([i] * int(file_blocks))
        disk_map.extend(["."] * int(space_blocks))

    disk_map_copy = disk_map.copy()

    for i, file_id in enumerate(disk_map):
        # Loop backwards through the disk map copy removing . until we reach a file ID
        # whilst making sure we don't reverse backwards past where we are going forwards
        while disk_map_copy[-1] == ".":
            disk_map_copy.pop()
        if len(disk_map_copy) <= i:
            break

        if file_id == ".":
            file_id = disk_map_copy.pop()
            disk_map[i] = file_id

        answer += i * file_id

    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
