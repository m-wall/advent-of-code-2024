def is_level_safe(levels):

    direction = None

    for x in range(1, len(levels)):
        current = levels[x - 1]
        next = levels[x]

        if current == next:
            return False
        if abs(current - next) > 3:
            return False
        if direction is None:
            direction = True if next > current else False
            continue
        current_direction = True if next > current else False
        if current_direction != direction:
            return False

    return True

def solve(puzzle_input):
    answer = 0
    lines = puzzle_input.splitlines()

    for line in lines:
        levels = [int(y) for y in line.split(" ")]

        if is_level_safe(levels):
            answer += 1
    
    return answer

if __name__ == '__main__':
    from timeit import default_timer
    start_time = default_timer()
    with open('input.txt', 'r', encoding="utf-8") as file:
        data = file.read()
    print(f'\nAnswer: {solve(data)}')
    print(f'\nSeconds: {default_timer() - start_time}\n')