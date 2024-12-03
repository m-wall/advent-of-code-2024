import os
import part1
import part2

test1 = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''

assert part1.solve(test1) == 161

test2 = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

assert part2.solve(test2) == 48

cwd = os.getcwd().split('\\')[-1]
print(f'****************** Day {cwd} Tests Successful :-) ******************')