def get_antenna_locations(matrix):
    locations = {}
    for r, row in enumerate(matrix):
        for c, col in enumerate(row):
            if col != ".":
                locations[(r, c)] = col
    return locations

def is_inbounds(position, matrix):
    return 0 <= position[0] < len(matrix) and 0 <= position[1] < len(matrix[0])

def get_antinodes_for_antenna_type(locations, matrix):
    antinodes = []

    for idx, loc_1 in enumerate(locations):
        for loc_2 in locations[idx+1:]:
            r1, c1 = loc_1
            r2, c2 = loc_2

            # Row and column distances between each antenna
            dr = r2 - r1
            dc = c2 - c1

            # Calculate the coordinates of the extended points
            loc_3 = ((r1 - dr), (c1 - dc))
            loc_4 = ((r2 + dr), (c2 + dc))

            # Check and add only if in bounds
            if is_inbounds(loc_3, matrix): antinodes.append(loc_3)
            if is_inbounds(loc_4, matrix): antinodes.append(loc_4)

    return antinodes

def solve(puzzle_input):
    matrix = [list(x) for x in puzzle_input.splitlines()]

    unique_antennas = set()
    for char in puzzle_input:
        if char not in [".", "\n"]:
            unique_antennas.add(char)

    all_antenna_locations = get_antenna_locations(matrix)

    antinodes = set()
    for antenna in unique_antennas:
        filtered_locations = [item for item, value in all_antenna_locations.items() if value == antenna]
        antinodes.update(get_antinodes_for_antenna_type(filtered_locations, matrix))

    return len(antinodes)

if __name__ == '__main__':
    from timeit import default_timer
    start_time = default_timer()
    with open('input.txt', 'r', encoding="utf-8") as file:
        data = file.read()
    print(f'\nAnswer: {solve(data)}')
    print(f'\nSeconds: {default_timer() - start_time}\n')