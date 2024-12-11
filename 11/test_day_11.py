def test_part_1():
    import day_11_part1

    test1 = '0 1 10 99 999'

    assert day_11_part1.solve(test1, 1) == 7

    test2 = '125 17'

    assert day_11_part1.solve(test2, 6) == 22
    assert day_11_part1.solve(test2, 25) == 55312

def test_part_2():
    import day_11_part2

    test1 = '0 1 10 99 999'

    assert day_11_part2.solve(test1, 1) == 7

    test2 = '125 17'

    assert day_11_part2.solve(test2, 6) == 22
    assert day_11_part2.solve(test2, 25) == 55312


if __name__ == '__main__':
    test_part_1()
    test_part_2()