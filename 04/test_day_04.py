def test_part_1():
    import day_04_part1

    test1 = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''

    assert day_04_part1.solve(test1) == 18


def test_part_2():
    import day_04_part2

    test2 = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''

    assert day_04_part2.solve(test2) == 9


if __name__ == '__main__':
    test_part_1()
    test_part_2()