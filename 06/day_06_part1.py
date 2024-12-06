DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def change_direction(current_direction):
    current_direction_index = DIRECTIONS.index(current_direction)
    next_direction_index = (current_direction_index + 1) % len(DIRECTIONS)
    return DIRECTIONS[next_direction_index]

def is_inbounds(position, matrix):
    return 0 <= position[0] < len(matrix) and 0 <= position[1] < len(matrix[0])

def find_patrol_positions(start, matrix):
    positions = {start}
    direction = DIRECTIONS[0]
    current_position = start

    while True:
        next_position = (current_position[0] + direction[0], current_position[1] + direction[1])

        if is_inbounds(next_position, matrix):

            if matrix[next_position[0]][next_position[1]] == "#":
                direction = change_direction(direction)
                continue

            current_position = next_position
            positions.add(current_position)
        else:
            break

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

    answer = len(positions)
    return answer

if __name__ == '__main__':
    from timeit import default_timer
    start_time = default_timer()
    with open('input.txt', 'r', encoding="utf-8") as file:
        data = file.read()
    print(f'\nAnswer: {solve(data)}')
    print(f'\nSeconds: {default_timer() - start_time}\n')