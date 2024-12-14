from aoc.helpers import grid
from aoc.helpers.decorators import timer


def get_valid_neighbours(current_position, previous_position, current_value, matrix):
    valid_neighbours = list()
    for neighbour in grid.get_neighbours(current_position, grid.ORTHOGONAL_DIRECTIONS):
        if not grid.is_in_grid_bounds(neighbour, matrix):
            continue
        if neighbour == previous_position:
            continue
        next_value = matrix[neighbour[0]][neighbour[1]]
        if next_value != current_value:
            continue
        valid_neighbours.append(neighbour)
    return valid_neighbours


def find_all_garden_plots(matrix):
    seen = set()
    plots = list()

    for r_idx, row in enumerate(matrix):
        for c_idx, plant in enumerate(row):
            start = (r_idx, c_idx)
            if start in seen:
                continue

            plot = set()
            path_queue = [(start, start)]

            while path_queue:
                current_position, previous_position = path_queue.pop()
                if current_position in seen:
                    continue

                seen.add(current_position)
                plot.add(current_position)

                neighbours = get_valid_neighbours(current_position, previous_position, plant, matrix)
                for neighbour in neighbours:
                    path_queue.append((neighbour, current_position))

            plots.append(plot)

    return plots


def rotate_plot(plot):
    max_r = max(r for r, _ in plot)
    rotated_squares = set()
    for r, c in plot:
        new_r = c
        new_c = max_r - r
        rotated_squares.add((new_r, new_c))
    return rotated_squares


def get_row_sides(plot, matrix):
    sides = 0
    for r in range(len(matrix)):
        on_upper_edge, on_lower_edge = False, False
        for c in range(len(matrix[0])):
            if (r, c) not in plot:
                on_upper_edge, on_lower_edge = False, False
                continue
            up = (r - 1, c)
            if up not in plot and not on_upper_edge:
                sides += 1
                on_upper_edge = True
            elif up in plot:
                on_upper_edge = False

            down = (r + 1, c)
            if down not in plot and not on_lower_edge:
                sides += 1
                on_lower_edge = True
            elif down in plot:
                on_lower_edge = False
    return sides


def plot_sides(plot, matrix):
    sides = 0
    sides += get_row_sides(plot, matrix)
    plot = rotate_plot(plot)
    sides += get_row_sides(plot, matrix)
    return sides


def solve(puzzle_input):
    answer = 0
    lines = puzzle_input.splitlines()
    matrix = [[char for char in line] for line in lines]
    for plot in find_all_garden_plots(matrix):
        answer += plot_sides(plot, matrix) * len(plot)
    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
