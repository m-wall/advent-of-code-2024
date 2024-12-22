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


def get_secret_ones(secret_number, n):
    ones = [secret_number % 10]
    result = secret_number
    for _ in range(n):
        result = next_secret(result)
        ones.append(result % 10)
    return ones


def solve(puzzle_input):
    answer = 0
    lines = puzzle_input.splitlines()

    banana_totals_per_sequence = {}

    for line in lines:
        ones = get_secret_ones(int(line), 2000)

        sequences = set()
        for i in range(len(ones) - 4):
            s1, s2, s3, s4, s5 = ones[i : i + 5]
            delta_sequence = (s2 - s1, s3 - s2, s4 - s3, s5 - s4)

            if delta_sequence in sequences:
                continue
            sequences.add(delta_sequence)

            if delta_sequence not in banana_totals_per_sequence:
                banana_totals_per_sequence[delta_sequence] = 0

            banana_totals_per_sequence[delta_sequence] += s5

    answer = max(banana_totals_per_sequence.values())
    return answer


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
