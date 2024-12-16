from collections import defaultdict
from heapq import heappop, heappush

from aoc.helpers import grid
from aoc.helpers.decorators import timer


def get_valid_neighbours(cost, position, direction, path, matrix):
    neighbours = list()
    opposite_direction = (-direction[0], -direction[1])
    for next_direction in grid.ORTHOGONAL_DIRECTIONS:
        if next_direction == opposite_direction:
            continue
        next_position, next_value = grid.next_position_and_value(position, next_direction, matrix)
        if next_value == "#":
            continue
        new_path = path + [next_position]
        if next_direction == direction:
            neighbours.append((cost + 1, next_position, next_direction, new_path))
        else:
            neighbours.append((cost + 1001, next_position, next_direction, new_path))
    return neighbours


def find_cheapest_path(start, end, matrix):
    path_queue = []
    heappush(path_queue, (0, start, grid.RIGHT, [start]))

    lowest_path_cost = float("inf")
    lowest_path_nodes = set()
    min_cost_to_node = defaultdict(lambda: float("inf"))

    while path_queue:
        cost, position, direction, path = heappop(path_queue)

        if position == end:
            if cost < lowest_path_cost:
                lowest_path_cost = cost
                lowest_path_nodes = set(path)
            elif cost == lowest_path_cost:
                lowest_path_nodes.update(path)
            continue

        if cost > min_cost_to_node[(position, direction)]:
            continue

        min_cost_to_node[(position, direction)] = cost

        neighbours = get_valid_neighbours(cost, position, direction, path, matrix)
        for neighbour in neighbours:
            new_cost = neighbour[0]
            if new_cost <= lowest_path_cost:
                heappush(path_queue, neighbour)

    return len(lowest_path_nodes)


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
