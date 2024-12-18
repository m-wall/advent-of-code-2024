from collections import deque

from aoc.helpers import grid
from aoc.helpers.decorators import timer


def find_shortest_path(byte_locations, start, end, dimension):
    seen = set()
    path_queue = deque([(start, 0)])

    while path_queue:
        current_position, steps = path_queue.popleft()

        for direction in grid.ORTHOGONAL_DIRECTIONS:
            next_position = grid.move(current_position, direction)
            if next_position in byte_locations or next_position in seen:
                continue
            if grid.is_in_bounds(next_position, dimension + 1, dimension + 1):
                if next_position == end:
                    return steps + 1
                seen.add(next_position)
                path_queue.append((next_position, steps + 1))

    return 0


def solve(puzzle_input, dimension):
    byte_locations = [(int(line.split(",")[1]), int(line.split(",")[0])) for line in puzzle_input.splitlines()]
    for num_bytes in range(1, len(byte_locations) + 1):
        result = find_shortest_path(set(byte_locations[:num_bytes]), (0, 0), (dimension, dimension), dimension)
        if result == 0:
            byte = byte_locations[num_bytes - 1]
            return f"{byte[1]},{byte[0]}"
    return 0


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data, 70)}")


if __name__ == "__main__":
    main()
