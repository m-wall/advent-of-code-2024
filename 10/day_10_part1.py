from heapq import heappush, heappop

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def is_inbounds(position, matrix):
    return 0 <= position[0] < len(matrix) and 0 <= position[1] < len(matrix[0])

def get_valid_neighbours(current_position, previous_position, matrix):
    neighbours = []
    current_value = matrix[current_position[0]][current_position[1]]

    for direction in DIRECTIONS:
        next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        if not is_inbounds(next_position, matrix): continue
        if next_position == previous_position: continue
        next_value = matrix[next_position[0]][next_position[1]]
        if next_value != current_value + 1: continue
        neighbours.append(next_position)

    return neighbours

def get_num_paths_for_trail_head(start, matrix):
    target_seen = set()
    path_seen = set()
    path_queue = []

    heappush(path_queue, (start, start))    # Tuple: current_position, previous_position

    while path_queue:
        current_position, previous_position = heappop(path_queue)
        current_value = matrix[current_position[0]][current_position[1]]
        
        if current_value == 9:
            target_seen.add(current_position)

        if (current_position, previous_position) in path_seen:
            continue
        path_seen.add((current_position, previous_position))

        neighbours = get_valid_neighbours(current_position, previous_position, matrix)
        for neighbour in neighbours:
            heappush(path_queue, (neighbour, current_position))

    return len(target_seen)

def solve(puzzle_input):
    answer = 0
    lines = puzzle_input.splitlines()
    matrix = [[int(char) for char in line] for line in lines]

    trail_heads = []
    for r, row in enumerate(matrix):
        for c, col in enumerate(row):
            if col == 0:
                trail_heads.append((r,c))

    for trail_head in trail_heads:
        answer += get_num_paths_for_trail_head(trail_head, matrix)

    return answer

if __name__ == '__main__':
    from timeit import default_timer
    start_time = default_timer()
    with open('input.txt', 'r', encoding="utf-8") as file:
        data = file.read()
    print(f'\nAnswer: {solve(data)}')
    print(f'\nSeconds: {default_timer() - start_time}\n')