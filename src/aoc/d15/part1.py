from aoc.helpers import grid
from aoc.helpers.decorators import timer

BOX = "O"
WALL = "#"
SPACE = "."
ROBOT = "@"
DIRECTIONS = {"^": grid.UP, "v": grid.DOWN, "<": grid.LEFT, ">": grid.RIGHT}


def push_boxes(box_position, direction, matrix):
    next_position, next_value = grid.next_position_and_value(box_position, direction, matrix)
    if next_value == WALL:
        return False
    if next_value == SPACE:
        grid.set_value(next_position, matrix, BOX)
        return True
    return push_boxes(next_position, direction, matrix)


def perform_moves(current_position, moves, matrix):
    for move in moves:
        next_position, next_value = grid.next_position_and_value(current_position, DIRECTIONS[move], matrix)
        if next_value == WALL:
            continue
        if next_value == BOX:
            if not push_boxes(next_position, DIRECTIONS[move], matrix):
                continue
        grid.set_value(next_position, matrix, ROBOT)
        grid.set_value(current_position, matrix, SPACE)
        current_position = next_position


def solve(puzzle_input):
    answer = 0
    map, moves = puzzle_input.split("\n\n")

    matrix = [[char for char in line] for line in map.splitlines()]
    moves = moves.replace("\n", "")

    start = grid.find_item_location("@", matrix)
    perform_moves(start, moves, matrix)

    for r, row in enumerate(matrix):
        for c, element in enumerate(row):
            if element == "O":
                answer += r * 100 + c
    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
