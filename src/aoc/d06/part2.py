from aoc.helpers import grid
from aoc.helpers.decorators import timer


def change_direction(current_direction):
    current_direction_index = grid.ORTHOGONAL_DIRECTIONS.index(current_direction)
    next_direction_index = (current_direction_index + 1) % len(grid.ORTHOGONAL_DIRECTIONS)
    return grid.ORTHOGONAL_DIRECTIONS[next_direction_index]


def is_patrol_loop(start, matrix):
    positions = {start: 1}
    direction = grid.ORTHOGONAL_DIRECTIONS[0]
    current_position = start

    while True:
        next_position = (
            current_position[0] + direction[0],
            current_position[1] + direction[1],
        )
        if not grid.is_in_grid_bounds(next_position, matrix):
            return False

        if matrix[next_position[0]][next_position[1]] == "#":
            direction = change_direction(direction)
            continue

        # Record the number of times we see each position
        positions[next_position] = positions.get(next_position, 0) + 1

        # If we see the same position more than 4 times return true
        # We must have at come at it from possibly each direction once
        # and/or the same direction more than once
        if positions[next_position] > 4:
            return True
        current_position = next_position


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
    answer = 0
    matrix = [list(x) for x in puzzle_input.splitlines()]

    start = find_start(matrix)
    positions = find_patrol_positions(start, matrix)

    # Only pass positions we know would have been walked as potential loop creating
    # obstacle positions. Cuts down the brute force approach of trying all
    for position in positions:
        matrix[position[0]][position[1]] = "#"
        answer += is_patrol_loop(start, matrix)
        matrix[position[0]][position[1]] = "."
    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
