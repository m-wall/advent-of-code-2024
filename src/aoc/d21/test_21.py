from pathlib import Path

import pytest

current_dir = Path(__file__).parent.resolve()


def test_part_1():
    from aoc.d21 import part1

    with open(current_dir / "sample1.txt", "r", encoding="utf-8") as file:
        sample1 = file.read()
    assert part1.solve(sample1) == 126384


@pytest.mark.skip
def test_part_2():
    from aoc.d21 import part2

    with open(current_dir / "sample1.txt", "r", encoding="utf-8") as file:
        sample1 = file.read()
    assert part2.solve(sample1) == 157908


if __name__ == "__main__":
    test_part_1()
    test_part_2()