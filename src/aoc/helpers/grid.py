from typing import List, Tuple, TypeVar

T = TypeVar("T")

"""
Represents orthogonal and diagonal directions as tuples.
For a row / column based 2D grid with (0, 0) top left
"""
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
UP_LEFT = (-1, -1)
UP_RIGHT = (-1, 1)
DOWN_LEFT = (1, -1)
DOWN_RIGHT = (1, 1)

ORTHOGONAL_DIRECTIONS = [UP, RIGHT, DOWN, LEFT]
DIAGONAL_DIRECTIONS = [UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT]
ALL_DIRECTIONS = [UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT]


def is_in_bounds(position: Tuple[int, int], row_max: int, col_max: int, row_min: int = 0, col_min: int = 0) -> bool:
    return row_min <= position[0] < row_max and col_min <= position[1] < col_max


def is_in_grid_bounds(position: Tuple[int, int], matrix: List[List[T]]) -> bool:
    return 0 <= position[0] < len(matrix) and 0 <= position[1] < len(matrix[0])


def get_neighbours(position: Tuple[int, int], directions: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return [(position[0] + direction[0], position[1] + direction[1]) for direction in directions]


def get_value(position: Tuple[int, int], matrix: List[List[T]]) -> T:
    return matrix[position[0]][position[1]]


def set_value(position: Tuple[int, int], matrix: List[List[T]], value: T):
    matrix[position[0]][position[1]] = value


def move(position: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
    return (position[0] + direction[0], position[1] + direction[1])


def next_position_and_value(
    position: Tuple[int, int], direction: Tuple[int, int], matrix: List[List[T]]
) -> Tuple[Tuple[int, int], T]:
    new_position = move(position, direction)
    return new_position, matrix[new_position[0]][new_position[1]]


def find_item_location(item, matrix: List[List[T]]):
    for r, row in enumerate(matrix):
        for c, element in enumerate(row):
            if element == item:
                return r, c
    return None


def print_grid(matrix: List[List[T]]):
    for row in matrix:
        print("".join(row))
    print("")


def print_coordinates_into_grid(coordinates: Tuple[int, int], max_row=None, max_col=None, fill_char="#"):
    if not max_row:
        max_row = max(row for row, _ in coordinates)
    if not max_col:
        max_col = max(col for _, col in coordinates)
    matrix = [["."] * (max_col + 1) for _ in range(max_row + 1)]
    for row, col in coordinates:
        matrix[row][col] = fill_char
    print_grid(matrix)
