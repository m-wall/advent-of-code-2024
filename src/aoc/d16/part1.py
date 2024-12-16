from heapq import heappop, heappush

from aoc.helpers import grid
from aoc.helpers.decorators import timer


def get_valid_neighbours(cost, position, direction, matrix):
    neighbours = list()
    opposite_direction = (-direction[0], -direction[1])
    for next_direction in grid.ORTHOGONAL_DIRECTIONS:
        if next_direction == opposite_direction:
            continue
        next_position, next_value = grid.next_position_and_value(position, next_direction, matrix)
        if next_value == "#":
            continue
        if next_direction == direction:
            neighbours.append((cost + 1, next_position, next_direction))
        else:
            neighbours.append((cost + 1001, next_position, next_direction))
    return neighbours


def find_cheapest_path(start, end, matrix):
    path_queue = []
    heappush(path_queue, (0, start, grid.RIGHT))

    seen = set()

    while path_queue:
        cost, position, direction = heappop(path_queue)

        if position == end:
            return cost

        if (position, direction) in seen:
            continue
        seen.add((position, direction))

        neighbours = get_valid_neighbours(cost, position, direction, matrix)
        for neighbour in neighbours:
            heappush(path_queue, neighbour)

    return 0


def solve(puzzle_input):
    lines = puzzle_input.splitlines()
    matrix = [list(line) for line in lines]
    start = grid.find_item_location("S", matrix)
    end = grid.find_item_location("E", matrix)
    return find_cheapest_path(start, end, matrix)


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
