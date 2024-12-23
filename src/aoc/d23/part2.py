import networkx as nx

from aoc.helpers.decorators import timer


def solve(puzzle_input):
    answer = 0
    lines = puzzle_input.splitlines()
    comp_pairs = [x.split("-") for x in lines]

    graph = nx.Graph()

    for a, b in comp_pairs:
        graph.add_edge(a, b)

    cliques = nx.find_cliques(graph)
    max_clique = max(cliques, key=len)

    answer = ",".join(sorted(max_clique))
    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
