from collections import defaultdict
from itertools import combinations

from aoc.helpers.decorators import timer


def solve(puzzle_input):
    answer = 0
    lines = puzzle_input.splitlines()
    comp_pairs = [x.split("-") for x in lines]

    connected = defaultdict(set)

    for a, b in comp_pairs:
        connected[a].add(b)
        connected[b].add(a)

    trios = set()
    for computer in connected:
        neighbors = connected[computer]
        for neighbor1, neighbor2 in combinations(neighbors, 2):
            if neighbor2 in connected[neighbor1]:
                trio = tuple(sorted([computer, neighbor1, neighbor2]))
                trios.add(trio)

    for trio in trios:
        for item in trio:
            if item[0] == "t":
                answer += 1
                break

    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
