from aoc.helpers.decorators import timer


def next_secret(secret_numer):
    result = secret_numer * 64
    secret_numer = result ^ secret_numer
    secret_numer = secret_numer % 16777216

    result = secret_numer // 32
    secret_numer = result ^ secret_numer
    secret_numer = secret_numer % 16777216

    result = secret_numer * 2048
    secret_numer = result ^ secret_numer
    secret_numer = secret_numer % 16777216

    return secret_numer


def find_nth_secret_number(secret_number, n):
    result = secret_number
    for _ in range(n):
        result = next_secret(result)
    return result


def solve(puzzle_input):
    answer = 0
    lines = puzzle_input.splitlines()

    for line in lines:
        answer += find_nth_secret_number(int(line), 2000)

    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
