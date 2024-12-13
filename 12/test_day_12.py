def test_part_1():
    import day_12_part1

    test1 = '''AAAA
BBCD
BBCC
EEEC'''

    assert day_12_part1.solve(test1) == 140

    test2 = '''OOOOO
OXOXO
OOOOO
OXOXO
OOOOO'''

    assert day_12_part1.solve(test2) == 772

    test3 = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''

    assert day_12_part1.solve(test3) == 1930


def test_part_2():
    import day_12_part2

    test1 = '''AAAA
BBCD
BBCC
EEEC'''

    assert day_12_part2.solve(test1) == 80

    test2 = '''OOOOO
OXOXO
OOOOO
OXOXO
OOOOO'''

    assert day_12_part2.solve(test2) == 436

    test3 = '''EEEEE
EXXXX
EEEEE
EXXXX
EEEEE'''

    assert day_12_part2.solve(test3) == 236

    test4 = '''AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA'''

    assert day_12_part2.solve(test4) == 368

    test5 = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''

    assert day_12_part2.solve(test5) == 1206


if __name__ == '__main__':
    test_part_1()
    test_part_2()