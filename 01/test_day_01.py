def test_part_1():
    import day_01_part1

    test1 = '''3   4
4   3
2   5
1   3
3   9
3   3'''

    assert day_01_part1.solve(test1) == 11


def test_part_2():
    import day_01_part2

    test2 = '''3   4
4   3
2   5
1   3
3   9
3   3'''

    assert day_01_part2.solve(test2) == 31

if __name__ == '__main__':
    test_part_1()
    test_part_2()
    