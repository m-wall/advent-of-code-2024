from aoc.helpers import grid
from aoc.helpers.decorators import timer

WALL = "#"
TRACK = "."
START = "S"
END = "E"


def get_track_positions_and_distance(matrix, start, end, benchmark):
    track_positions = {start: benchmark}
    current_position = start
    picoseconds = benchmark
    while current_position != end:
        for direction in grid.ORTHOGONAL_DIRECTIONS:
            next_position, value = grid.next_position_and_value(current_position, direction, matrix)
            if value == WALL:
                continue
            if next_position not in track_positions:
                picoseconds -= 1
                track_positions[next_position] = picoseconds
                current_position = next_position
                break
    return track_positions


def get_cheat_positions(current_position, matrix):
    seen = set()
    seen.add(current_position)
    cheat_locations = list()
    queue = [(current_position, 0)]

    while queue:
        position, distance = queue.pop(0)
        if distance >= 20:
            continue
        for direction in grid.ORTHOGONAL_DIRECTIONS:
            next_position = (position[0] + direction[0], position[1] + direction[1])
            if next_position in seen:
                continue
            seen.add(next_position)
            if not (0 <= next_position[0] < len(matrix) and 0 <= next_position[1] < len(matrix[0])):
                continue
            value = matrix[next_position[0]][next_position[1]]
            queue.append((next_position, distance + 1))
            if (value == TRACK or value == END) and distance > 0:
                cheat_locations.append((next_position, distance + 1))

    return cheat_locations


def race(matrix, start, end, benchmark, saving_required):
    completed = 0
    target_time = benchmark - saving_required
    track_positions = get_track_positions_and_distance(matrix, start, end, benchmark)

    for track_position in track_positions.keys():
        for cheat_position, cheat_distance in get_cheat_positions(track_position, matrix):
            total_time = benchmark - track_positions[track_position] + track_positions[cheat_position] + cheat_distance
            if total_time <= target_time:
                completed += 1
    return completed


def solve(puzzle_input, saving_required):
    answer = 0
    lines = puzzle_input.splitlines()

    benchmark = 1
    matrix = list()
    for line in lines:
        benchmark += line.count(".")
        matrix.append(list(line))

    start = grid.find_item_location("S", matrix)
    end = grid.find_item_location("E", matrix)

    answer = race(matrix, start, end, benchmark, saving_required)
    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data, 100)}")


if __name__ == "__main__":
    main()
