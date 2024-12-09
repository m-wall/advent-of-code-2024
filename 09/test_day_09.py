def test_part_1():
    import day_09_part1

    test1 = '''2333133121414131402'''

    assert day_09_part1.solve(test1) == 1928


def test_part_2():
    import day_09_part2

    test2 = '''2333133121414131402'''

    assert day_09_part2.solve(test2) == 2858


if __name__ == '__main__':
    test_part_1()
    test_part_2()