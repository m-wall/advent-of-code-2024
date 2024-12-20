from pathlib import Path

current_dir = Path(__file__).parent.resolve()


def test_part_1():
    from aoc.d20 import part1

    with open(current_dir / "sample1.txt", "r", encoding="utf-8") as file:
        sample1 = file.read()
    assert part1.solve(sample1, 2) == 44
    assert part1.solve(sample1, 10) == 10
    assert part1.solve(sample1, 38) == 3
    assert part1.solve(sample1, 64) == 1


def test_part_2():
    from aoc.d20 import part2

    with open(current_dir / "sample1.txt", "r", encoding="utf-8") as file:
        sample1 = file.read()
    assert part2.solve(sample1, 50) == 285
    assert part2.solve(sample1, 70) == 41
    assert part2.solve(sample1, 72) == 29
    assert part2.solve(sample1, 74) == 7
    assert part2.solve(sample1, 76) == 3


if __name__ == "__main__":
    test_part_1()
    test_part_2()
