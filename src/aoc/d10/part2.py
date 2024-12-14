from aoc.helpers import grid
from aoc.helpers.decorators import timer


def get_valid_neighbours(current_position, previous_position, matrix):
    neighbours = []
    current_value = matrix[current_position[0]][current_position[1]]

    for direction in grid.ORTHOGONAL_DIRECTIONS:
        next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        if not grid.is_in_grid_bounds(next_position, matrix):
            continue
        if next_position == previous_position:
            continue
        next_value = matrix[next_position[0]][next_position[1]]
        if next_value != current_value + 1:
            continue
        neighbours.append(next_position)

    return neighbours


def get_num_paths_for_trail_head(start, matrix):
    target_seen = 0
    path_queue = [(start, start)]

    while path_queue:
        current_position, previous_position = path_queue.pop()
        current_value = matrix[current_position[0]][current_position[1]]

        if current_value == 9:
            target_seen += 1

        neighbours = get_valid_neighbours(current_position, previous_position, matrix)
        for neighbour in neighbours:
            path_queue.append((neighbour, current_position))

    return target_seen


def solve(puzzle_input):
    answer = 0
    lines = puzzle_input.splitlines()
    matrix = [[int(char) for char in line] for line in lines]

    trail_heads = []
    for r, row in enumerate(matrix):
        for c, col in enumerate(row):
            if col == 0:
                trail_heads.append((r, c))

    for trail_head in trail_heads:
        answer += get_num_paths_for_trail_head(trail_head, matrix)

    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
