def test_part_1():
    import day_03_part1

    test1 = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''

    assert day_03_part1.solve(test1) == 161


def test_part_2():
    import day_03_part2

    test2 = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

    assert day_03_part2.solve(test2) == 48


if __name__ == '__main__':
    test_part_1()
    test_part_2()
