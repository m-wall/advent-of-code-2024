from aoc.helpers import grid
from aoc.helpers.decorators import timer

BOX = ["[", "]"]
WALL = "#"
SPACE = "."
ROBOT = "@"
DIRECTIONS = {"^": grid.UP, "v": grid.DOWN, "<": grid.LEFT, ">": grid.RIGHT}


def push_boxes_horizontal(box_half_a_pos, direction, matrix):
    box_half_b_pos, box_half_b_val = grid.next_position_and_value(box_half_a_pos, direction, matrix)
    target_position, target_value = grid.next_position_and_value(box_half_b_pos, direction, matrix)
    if target_value == WALL:
        return False
    if target_value in BOX:
        if not push_boxes_horizontal(target_position, direction, matrix):
            return False
    grid.set_value(target_position, matrix, box_half_b_val)
    grid.set_value(box_half_b_pos, matrix, grid.get_value(box_half_a_pos, matrix))
    return True


def can_box_move_vertical(box_half_a_pos, direction, matrix):
    box_half_a_val = grid.get_value(box_half_a_pos, matrix)
    box_half_b_direction = grid.RIGHT if box_half_a_val == "[" else grid.LEFT
    box_half_b_pos = grid.move(box_half_a_pos, box_half_b_direction)

    target_half_a_pos, target_half_a_val = grid.next_position_and_value(box_half_a_pos, direction, matrix)
    target_half_b_pos, target_half_b_val = grid.next_position_and_value(box_half_b_pos, direction, matrix)

    if WALL in [target_half_a_val, target_half_b_val]:
        return WALL
    if target_half_a_val in BOX or target_half_b_val in BOX:
        if target_half_a_val == box_half_a_val:
            return [target_half_a_pos]
        else:
            target_boxes = list()
            if target_half_a_val in BOX:
                target_boxes.append(target_half_a_pos)
            if target_half_b_val in BOX:
                target_boxes.append(target_half_b_pos)
            return target_boxes
    return SPACE


def push_boxes_vertical(boxes, direction, matrix):
    new_boxes = set()
    for box in boxes:
        result = can_box_move_vertical(box, direction, matrix)
        if result == WALL:
            return False
        if type(result) is list:
            new_boxes.update(result)

    if new_boxes:
        if not push_boxes_vertical(new_boxes, direction, matrix):
            return False

    # Made it here so boxes must be able to move
    box_list = list(boxes)
    for box_half_a_pos in box_list:
        box_half_a_val = grid.get_value(box_half_a_pos, matrix)
        box_half_b_direction = grid.RIGHT if box_half_a_val == "[" else grid.LEFT
        box_half_b_pos, box_half_b_val = grid.next_position_and_value(box_half_a_pos, box_half_b_direction, matrix)
        # Watch out for two halves of the same box in the list so that we don't process it twice
        if box_half_b_pos in boxes:
            box_list.remove(box_half_b_pos)
        grid.set_value(grid.move(box_half_a_pos, direction), matrix, box_half_a_val)
        grid.set_value(grid.move(box_half_b_pos, direction), matrix, box_half_b_val)
        grid.set_value(box_half_a_pos, matrix, SPACE)
        grid.set_value(box_half_b_pos, matrix, SPACE)
    return True


def perform_moves(current_position, moves, matrix):
    for move in moves:
        next_position, next_value = grid.next_position_and_value(current_position, DIRECTIONS[move], matrix)
        if next_value == WALL:
            continue
        if next_value in BOX:
            direction = DIRECTIONS[move]
            if direction in [grid.LEFT, grid.RIGHT]:
                if not push_boxes_horizontal(next_position, DIRECTIONS[move], matrix):
                    continue
            else:
                if not push_boxes_vertical([next_position], DIRECTIONS[move], matrix):
                    continue
        grid.set_value(next_position, matrix, ROBOT)
        grid.set_value(current_position, matrix, SPACE)
        current_position = next_position


def solve(puzzle_input):
    answer = 0
    map, moves = puzzle_input.split("\n\n")

    matrix = list()
    for line in map.splitlines():
        doubled_line = line.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
        matrix.append(list(doubled_line))

    moves = moves.replace("\n", "")

    start = grid.find_item_location("@", matrix)
    perform_moves(start, moves, matrix)

    for r, row in enumerate(matrix):
        for c, element in enumerate(row):
            if element == "[":
                answer += r * 100 + c
    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
