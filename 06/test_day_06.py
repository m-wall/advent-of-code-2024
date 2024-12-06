def test_part_1():
    import day_06_part1

    test1 = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

    assert day_06_part1.solve(test1) == 41


def test_part_2():
    import day_06_part2

    test2 = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

    assert day_06_part2.solve(test2) == 6


if __name__ == '__main__':
    test_part_1()
    test_part_2()