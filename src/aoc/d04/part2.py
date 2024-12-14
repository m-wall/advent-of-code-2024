from aoc.helpers.decorators import timer

SEARCH_STRING = "MAS"


def is_x_mas(matrix, row, col):
    # The starting position of the A in MAS cannot be an edge
    if row in [0, len(matrix) - 1] or col in [0, len(matrix[0]) - 1]:
        return False

    check_string = matrix[row - 1][col - 1] + "A" + matrix[row + 1][col + 1]
    if check_string not in [SEARCH_STRING, SEARCH_STRING[::-1]]:
        return False

    check_string = matrix[row + 1][col - 1] + "A" + matrix[row - 1][col + 1]
    return check_string in [SEARCH_STRING, SEARCH_STRING[::-1]]


def solve(puzzle_input):
    answer = 0
    matrix = puzzle_input.splitlines()

    for r_idx, row in enumerate(matrix):
        for c_idx, col in enumerate(row):
            if matrix[r_idx][c_idx] == "A":
                answer += is_x_mas(matrix, r_idx, c_idx)
    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
