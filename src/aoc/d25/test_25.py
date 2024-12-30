from pathlib import Path

current_dir = Path(__file__).parent.resolve()


def test_part_1():
    from aoc.d25 import part1

    with open(current_dir / "sample1.txt", "r", encoding="utf-8") as file:
        sample1 = file.read()
    assert part1.solve(sample1) == 3


def test_part_2():
    # There is no part 2 for day 25. Having completed all other days is the final gold star.
    # Just satisfying my OCD to make the test file complete and amount to 50!
    assert "Final gold star" == "Final gold star"


if __name__ == "__main__":
    test_part_1()
    test_part_2()
