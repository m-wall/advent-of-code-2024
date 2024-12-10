def test_part_1():
    import day_10_part1

    test1 = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''

    assert day_10_part1.solve(test1) == 36


def test_part_2():
    import day_10_part2

    test2 = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''

    assert day_10_part2.solve(test2) == 81


if __name__ == '__main__':
    test_part_1()
    test_part_2()