def test_part_1():
    import day_07_part1

    test1 = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

    assert day_07_part1.solve(test1) == 3749


def test_part_2():
    import day_07_part2

    test2 = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

    assert day_07_part2.solve(test2) == 11387


if __name__ == '__main__':
    test_part_1()
    test_part_2()