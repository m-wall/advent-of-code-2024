from aoc.helpers.decorators import timer


def find_future_posion(robot, n_rows, n_cols, seconds):
    pr, pc, vr, vc = robot
    total_r = vr * seconds + pr
    total_c = vc * seconds + pc
    return total_r % n_rows, total_c % n_cols


def quadrant_count(positions, min_r, min_c, max_r, max_c):
    count = 0
    for pr, pc in positions:
        if min_r <= pr < max_r and min_c <= pc < max_c:
            count += 1
    return count


def solve(puzzle_input, n_rows, n_cols, seconds):
    answer = 1
    lines = puzzle_input.splitlines()

    robots = list()
    for line in lines:
        line = line.replace("p=", "").replace(" v=", ",")
        pc, pr, vc, vr = tuple(int(num) for num in line.split(","))
        robots.append((pr, pc, vr, vc))

    final_positions = list()
    for robot in robots:
        final_positions.append(find_future_posion(robot, n_rows, n_cols, seconds))

    answer *= quadrant_count(final_positions, 0, 0, n_rows // 2, n_cols // 2)  # Top left
    answer *= quadrant_count(final_positions, 0, n_cols // 2 + 1, n_rows // 2, n_cols)  # Top right
    answer *= quadrant_count(final_positions, n_rows // 2 + 1, 0, n_rows, n_cols // 2)  # Bottom left
    answer *= quadrant_count(final_positions, n_rows // 2 + 1, n_cols // 2 + 1, n_rows, n_cols)  # Bottom right

    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data, 103, 101, 100)}")


if __name__ == "__main__":
    main()
