from pathlib import Path

current_dir = Path(__file__).parent.resolve()


def test_part_1():
    from aoc.d12 import part1

    with open(current_dir / "sample1.txt", "r", encoding="utf-8") as file:
        sample1 = file.read()
    assert part1.solve(sample1) == 140

    with open(current_dir / "sample2.txt", "r", encoding="utf-8") as file:
        sample2 = file.read()
    assert part1.solve(sample2) == 772

    with open(current_dir / "sample3.txt", "r", encoding="utf-8") as file:
        sample3 = file.read()
    assert part1.solve(sample3) == 1930


def test_part_2():
    from aoc.d12 import part2

    with open(current_dir / "sample1.txt", "r", encoding="utf-8") as file:
        sample1 = file.read()
    assert part2.solve(sample1) == 80

    with open(current_dir / "sample2.txt", "r", encoding="utf-8") as file:
        sample2 = file.read()
    assert part2.solve(sample2) == 436

    with open(current_dir / "sample3.txt", "r", encoding="utf-8") as file:
        sample3 = file.read()
    assert part2.solve(sample3) == 1206


if __name__ == "__main__":
    test_part_1()
    test_part_2()
