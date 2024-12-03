def test_part_1():
    import day_02_part1

    test1 = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

    assert day_02_part1.solve(test1) == 2


def test_part_2():
    import day_02_part2

    test2 = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

    assert day_02_part2.solve(test2) == 4


if __name__ == '__main__':
    test_part_1()
    test_part_2()
