from typing import List, Tuple, TypeVar

T = TypeVar("T")

"""
Represents cardinal and diagonal directions as tuples.
For a row / column based 2D matrix with 0,0 top left
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


def is_in_bounds(
    position: Tuple[int, int],
    row_max: int,
    col_max: int,
    row_min: int = 0,
    col_min: int = 0,
) -> bool:
    return row_min <= position[0] < row_max and col_min <= position[1] < col_max


def is_in_grid_bounds(position: Tuple[int, int], grid: List[List[T]]) -> bool:
    return 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0])


def get_neighbours(position: Tuple[int, int], directions: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return [(position[0] + direction[0], position[1] + direction[1]) for direction in directions]


def move(position: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
    return (position[0] + direction[0], position[1] + direction[1])


def print_grid(coordinates: Tuple[int, int], max_row=None, max_col=None, fill_char="#"):
    if not max_row:
        max_row = max(row for row, _ in coordinates)
    if not max_col:
        max_col = max(col for _, col in coordinates)

    grid = [["."] * (max_col) for _ in range(max_row)]

    for row, col in coordinates:
        grid[row][col] = fill_char

    for row in grid:
        print("".join(row))
    print("")
