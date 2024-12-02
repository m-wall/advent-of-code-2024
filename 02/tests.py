import os
import part1
import part2

test1 = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

assert part1.solve(test1) == 2

test2 = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

assert part2.solve(test2) == 4

cwd = os.getcwd().split('\\')[-1]
print(f'****************** Day {cwd} Tests Successful :-) ******************')