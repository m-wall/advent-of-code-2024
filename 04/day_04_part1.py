DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

SEARCH_STRING = "XMAS"

def count_xmas_from_position(matrix, row, col):
    found = 0
    row_max = len(matrix)
    col_max = len(matrix[0])
    search_string_length = len(SEARCH_STRING)

    for direction in DIRECTIONS:
        check_string = ""
        for x in range(0, search_string_length):
            target_row = row + (x * direction[0])
            target_col = col + (x * direction[1])
            if 0 <= target_row < row_max and 0 <= target_col < col_max:
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

if __name__ == '__main__':
    from timeit import default_timer
    start_time = default_timer()
    with open('input.txt', 'r', encoding="utf-8") as file:
        data = file.read()
    print(f'\nAnswer: {solve(data)}')
    print(f'\nSeconds: {default_timer() - start_time}\n')