from pathlib import Path

current_dir = Path(__file__).parent.resolve()


def test_part_1():
    from aoc.d22 import part1

    with open(current_dir / "sample1.txt", "r", encoding="utf-8") as file:
        sample1 = file.read()
    assert part1.solve(sample1) == 37327623


def test_part_2():
    from aoc.d22 import part2

    with open(current_dir / "sample2.txt", "r", encoding="utf-8") as file:
        sample2 = file.read()
    assert part2.solve(sample2) == 23


if __name__ == "__main__":
    test_part_1()
    test_part_2()
