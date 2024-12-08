import itertools

OPERATORS = ["+","*"]

def interleave_lists(numbers, operators):
    result = []
    for i in range(len(operators)):
        result.append(numbers[i])
        result.append(operators[i])
    result.append(numbers[-1])
    return result

def calc_equation(equation):
    expected, numbers = equation.split(":")
    numbers = [int(x) for x in numbers.split()]

    operator_combinations = list(itertools.product(OPERATORS, repeat=len(numbers) - 1))

    for operator_combination in operator_combinations:
        statement_list = interleave_lists(numbers,operator_combination)

        result = statement_list[0]
        for i in range(1, len(statement_list), 2):
            operator = statement_list[i]
            next_num = statement_list[i + 1]

            if operator == '+':
                result += next_num
            elif operator == '*':
                result *= next_num

        if result == int(expected):
           return result

    return 0


def solve(puzzle_input):
    answer = 0
    equations = puzzle_input.splitlines()

    for equation in equations:
        answer += calc_equation(equation)

    return answer

if __name__ == '__main__':
    from timeit import default_timer
    start_time = default_timer()
    with open('input.txt', 'r', encoding="utf-8") as file:
        data = file.read()
    print(f'\nAnswer: {solve(data)}')
    print(f'\nSeconds: {default_timer() - start_time}\n')