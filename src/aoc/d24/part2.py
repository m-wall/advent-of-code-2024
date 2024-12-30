from itertools import combinations

import networkx as nx

from aoc.helpers.decorators import timer


def calculate_value(a, op, b):
    if op == "AND":
        return a & b
    elif op == "OR":
        return a | b
    elif op == "XOR":
        return a ^ b


def run_device(values, connections, z_count):
    i = 0
    z_values_found = set()
    values = values.copy()
    while len(z_values_found) != z_count and i < 1000:
        i += 1
        for a, op, b, result in connections:
            if a in values and b in values:
                values[result] = calculate_value(values[a], op, values[b])
                if result[0] == "z":
                    z_values_found.add(result)

    values = dict(sorted(values.items(), reverse=True))
    z_values = [value for key, value in values.items() if key[0] == "z"]

    if len(z_values) == z_count:
        z = int("".join(map(str, z_values)), 2)
        return z
    else:
        return -9


def get_first_faulty_z(expected_z, calculated_z):
    expected_z_str = bin(expected_z)[2:]
    calculated_z_str = bin(calculated_z)[2:]

    max_len = max(len(expected_z_str), len(calculated_z_str))
    expected_z_str = expected_z_str.rjust(max_len, "x")
    calculated_z_str = calculated_z_str.rjust(max_len, "x")

    for i in range(max_len):
        if expected_z_str[-(i + 1)] != calculated_z_str[-(i + 1)]:
            return i + 1
    return -1


def swap_connections(connections, a, b):
    for i, connection in enumerate(connections):
        if connection[3] == a:
            connections[i][3] = b
        elif connection[3] == b:
            connections[i][3] = a


def ancestors_within_depth(graph, node, depth):
    ancestors = set()
    current_depth = 0
    queue = [(node, current_depth)]
    while queue:
        current_node, current_depth = queue.pop(0)
        if current_depth > depth:
            continue
        for parent in graph.predecessors(current_node):
            ancestors.add(parent)
            if current_depth + 1 <= depth:
                queue.append((parent, current_depth + 1))
    return ancestors


def get_unique_ancestors(graph, connections, faulty_z, depth):
    z_wire = f"z{str(faulty_z).zfill(2)}"
    ancestors = ancestors_within_depth(graph, z_wire, depth)
    for n in range(depth):
        ancestors.add(f"z{str(faulty_z - n).zfill(2)}")
    diff = [item for item in ancestors if item in [connection[3] for connection in connections]]
    return diff


def find_swaps(connections, values, graph, expected_z, z_count):
    best_swaps = []

    calculated_z = run_device(values, connections, z_count)
    if calculated_z == expected_z:
        return best_swaps

    cur_faulty_z = get_first_faulty_z(expected_z, calculated_z)
    print(f"Calculated z: {calculated_z}, Expected z: {expected_z}, Faulty z: {cur_faulty_z}")

    possible_swaps = get_unique_ancestors(graph, connections, cur_faulty_z, 2)

    max_faulty_z = cur_faulty_z
    test_values, expected_z = generate_test_values(45)

    for a, b in combinations(possible_swaps, 2):
        swap_connections(connections, a, b)
        calculated_z = run_device(test_values, connections, 45)
        new_faulty_z = get_first_faulty_z(expected_z, calculated_z)
        if new_faulty_z > max_faulty_z:
            best_swaps = [[a, b]]
            max_faulty_z = new_faulty_z
        elif new_faulty_z == max_faulty_z:
            best_swaps.append([a, b])
        swap_connections(connections, b, a)

    return best_swaps


def generate_test_values(length):
    values = {}
    for i in range(length + 1):
        values[f"x{str(i).zfill(2)}"] = i % 2
        values[f"y{str(i).zfill(2)}"] = (i + 1) % 2

    values = dict(sorted(values.items(), reverse=True))
    x_values = [value for key, value in values.items() if key[0] == "x"]
    y_values = [value for key, value in values.items() if key[0] == "y"]
    x_bin_str = "".join(map(str, x_values))
    y_bin_str = "".join(map(str, y_values))
    x = int(x_bin_str, 2)
    y = int(y_bin_str, 2)
    expected_z = x + y
    return values, expected_z


def solve(puzzle_input):
    _, connections = puzzle_input.split("\n\n")
    connections = [connection.replace("-> ", "").split(" ") for connection in connections.strip().split("\n")]

    graph = nx.DiGraph()
    for a, _, b, result in connections:
        graph.add_edge(a, result)
        graph.add_edge(b, result)

    swap_connections(connections, "z10", "mwk")
    swap_connections(connections, "z18", "qgd")
    swap_connections(connections, "hsw", "jmh")
    swap_connections(connections, "z33", "gqp")

    for i in range(1, 45):
        test_values, expected_z = generate_test_values(i)
        z_len = len(bin(expected_z)) - 2
        possible_swaps = find_swaps(connections, test_values, graph, expected_z, z_len)
        if possible_swaps:
            print(f"Possible swaps: {possible_swaps}\n")
            break

    answer = ",".join(sorted(["z10", "mwk", "z18", "qgd", "hsw", "jmh", "z33", "gqp"]))
    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
