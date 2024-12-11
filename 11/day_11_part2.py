import functools

@functools.cache
def process_stone(stone, blinks):

    if blinks == 0:
        return 1
    
    if stone == 0:
        return process_stone(1, blinks - 1)
    if len(str(stone)) % 2 == 0:
        stone = str(stone)
        midpoint = len(stone) // 2
        left = int(stone[:midpoint])
        right = int(stone[midpoint:])
        return process_stone(left, blinks - 1) + process_stone(right, blinks - 1)
    
    return process_stone(stone * 2024, blinks - 1)

def solve(puzzle_input, blinks):
    answer = 0
    stones = [int(num) for num in puzzle_input.split()]

    for stone in stones:
        answer += process_stone(stone, blinks)

    return answer

if __name__ == '__main__':
    from timeit import default_timer
    start_time = default_timer()
    with open('input.txt', 'r', encoding="utf-8") as file:
        data = file.read()
    print(f'\nAnswer: {solve(data, 75)}')
    print(f'\nSeconds: {default_timer() - start_time}\n')