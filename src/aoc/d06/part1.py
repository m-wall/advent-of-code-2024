from aoc.helpers import grid
from aoc.helpers.decorators import timer


def change_direction(current_direction):
    current_direction_index = grid.ORTHOGONAL_DIRECTIONS.index(current_direction)
    next_direction_index = (current_direction_index + 1) % len(grid.ORTHOGONAL_DIRECTIONS)
    return grid.ORTHOGONAL_DIRECTIONS[next_direction_index]


def find_patrol_positions(start, matrix):
    positions = {start}
    direction = grid.ORTHOGONAL_DIRECTIONS[0]
    current_position = start

    while True:
        next_position = (
            current_position[0] + direction[0],
            current_position[1] + direction[1],
        )
        if not grid.is_in_grid_bounds(next_position, matrix):
            break

        if matrix[next_position[0]][next_position[1]] == "#":
            direction = change_direction(direction)
            continue
        current_position = next_position
        positions.add(current_position)

    return positions


def find_start(matrix):
    for r_idx, row in enumerate(matrix):
        for c_idx, col in enumerate(row):
            if col == "^":
                return (r_idx, c_idx)
    return None


def solve(puzzle_input):
    matrix = [list(x) for x in puzzle_input.splitlines()]
    start = find_start(matrix)
    positions = find_patrol_positions(start, matrix)
    return len(positions)


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
