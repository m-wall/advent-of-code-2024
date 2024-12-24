from functools import cache
from itertools import product

from aoc.helpers import grid
from aoc.helpers.decorators import timer

NUM_PAD = (("7", "8", "9"), ("4", "5", "6"), ("1", "2", "3"), ("#", "0", "A"))
DIR_PAD = (("#", "^", "A"), ("<", "v", ">"))

KEY_DIRS = {grid.UP: "^", grid.DOWN: "v", grid.LEFT: "<", grid.RIGHT: ">"}


@cache
def count_segments(path):
    if not path:
        return 0
    segments = 1
    for i in range(1, len(path)):
        if path[i] != path[i - 1]:
            segments += 1
    return segments


@cache
def shortest_pad_moves(start, end, pad):
    possible_steps = []
    visited = set()

    start_position = grid.find_item_location(start, pad)
    end_position = grid.find_item_location(end, pad)

    queue = [(start_position, 0, "")]

    while queue:
        current_pos, steps, path = queue.pop(0)
        if current_pos == end_position:
            path += "A"
            possible_steps.append(path)
        visited.add(current_pos)
        for direction in grid.ORTHOGONAL_DIRECTIONS:
            next_pos = grid.move(current_pos, direction)
            if grid.is_in_grid_bounds(next_pos, pad) and next_pos not in visited:
                next_value = grid.get_value(next_pos, pad)
                if next_value != "#":
                    queue.append((next_pos, steps + 1, path + KEY_DIRS[direction]))

    min_segments = min(count_segments(step) for step in possible_steps)
    filtered_steps = [step for step in possible_steps if count_segments(step) == min_segments]

    return sorted(filtered_steps)


@cache
def button_combinations(input, pad):
    key_options = []
    previous_button = "A"
    for button in input:
        moves = shortest_pad_moves(previous_button, button, pad)
        key_options.append(moves)
        previous_button = button

    return ["".join(x) for x in product(*key_options)]


def solve(puzzle_input):
    answer = 0
    lines = puzzle_input.splitlines()

    for code in lines:
        robot_0_options = button_combinations(code, NUM_PAD)

        robot_1_options = []
        for option in robot_0_options:
            robot_1_options.extend(button_combinations(option, DIR_PAD))

        robot_2_options = []
        for option in robot_1_options:
            robot_2_options.extend(button_combinations(option, DIR_PAD))

        min_buttons = min(map(len, robot_2_options))
        answer += min_buttons * int(code[:-1])

    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()