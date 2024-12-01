import os
import part1
import part2

test1 = '''3   4
4   3
2   5
1   3
3   9
3   3'''

assert part1.solve(test1) == 11

test2 = '''3   4
4   3
2   5
1   3
3   9
3   3'''

assert part2.solve(test2) == 31

cwd = os.getcwd().split('\\')[-1]
print(f'****************** Day {cwd} Tests Successful :-) ******************')