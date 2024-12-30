from aoc.helpers.decorators import timer


def calculate_value(a, op, b):
    if op == "AND":
        return a & b
    elif op == "OR":
        return a | b
    elif op == "XOR":
        return a ^ b


def solve(puzzle_input):
    answer = 0
    wires, connections = puzzle_input.split("\n\n")

    values = {wire.split(": ")[0]: int(wire.split(": ")[1]) for wire in wires.split("\n")}
    connections = [connection.replace("-> ", "").split(" ") for connection in connections.strip().split("\n")]

    z_count = sum(1 for x, y, op, r in connections if r.startswith("z"))

    while len([key for key in values.keys() if key.startswith("z")]) != z_count:
        for a, op, b, result in connections:
            if a in values and b in values:
                values[result] = calculate_value(values[a], op, values[b])
            else:
                continue

    z_keys = sorted([key for key in values.keys() if key.startswith("z")], reverse=True)
    z_values = [values[key] for key in z_keys]
    binary_string = "".join(map(str, z_values))
    answer = int(binary_string, 2)

    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
