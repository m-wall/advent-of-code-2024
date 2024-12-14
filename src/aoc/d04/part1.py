from aoc.helpers import grid
from aoc.helpers.decorators import timer

SEARCH_STRING = "XMAS"


def count_xmas_from_position(matrix, row, col):
    found = 0

    for direction in grid.ALL_DIRECTIONS:
        check_string = ""
        for x in range(0, len(SEARCH_STRING)):
            target_row = row + (x * direction[0])
            target_col = col + (x * direction[1])
            if grid.is_in_grid_bounds((target_row, target_col), matrix):
                check_string += matrix[target_row][target_col]
            else:
                break
        if check_string == SEARCH_STRING:
            found += 1
    return found


def solve(puzzle_input):
    answer = 0
    matrix = puzzle_input.splitlines()

    for r_idx, row in enumerate(matrix):
        for c_idx, col in enumerate(row):
            if matrix[r_idx][c_idx] == "X":
                answer += count_xmas_from_position(matrix, r_idx, c_idx)
    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
