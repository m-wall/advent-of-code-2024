from aoc.helpers.decorators import timer


def get_matching_slices_from_index(design, index, towels, max_towel_length):
    matched_slices = []
    for i in range(1, max_towel_length + 1):
        if index + i > len(design):
            break
        slice = design[index : index + i]
        if slice in towels:
            matched_slices.append((slice, index))
    return matched_slices


def solve(puzzle_input):
    answer = 0
    towels, designs = puzzle_input.split("\n\n")
    towels = set(towels.split(", "))
    designs = designs.split("\n")

    max_towel_length = len(max(towels, key=len))

    for design in designs:
        seen = set()
        design_slices = []
        design_slices.extend(get_matching_slices_from_index(design, 0, towels, max_towel_length))

        while design_slices:
            slice, index = design_slices.pop()

            if index + len(slice) == len(design):
                answer += 1
                break

            if (slice, index) in seen:
                continue
            seen.add((slice, index))

            design_slices.extend(get_matching_slices_from_index(design, index + len(slice), towels, max_towel_length))

    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
