from aoc.helpers.decorators import timer


def process_stones(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
            continue
        if len(str(stone)) % 2 == 0:
            stone = str(stone)
            midpoint = len(stone) // 2
            new_stones.append(int(stone[:midpoint]))
            new_stones.append(int(stone[midpoint:]))
            continue
        new_stones.append(stone * 2024)
    return new_stones


def solve(puzzle_input, blinks):
    stones = [int(num) for num in puzzle_input.split()]
    for _ in range(blinks):
        stones = process_stones(stones)
    return len(stones)


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data, 25)}")


if __name__ == "__main__":
    main()
