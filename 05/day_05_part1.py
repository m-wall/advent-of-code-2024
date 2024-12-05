def solve(puzzle_input):
    answer = 0
    rules_str, updates_str = puzzle_input.split("\n\n")

    rules = [x.split("|") for  x in rules_str.splitlines()]
    updates = [x.split(",") for  x in updates_str.splitlines()]

    for update in updates:
        for x, y in rules:
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    break
        else:
            answer += int(update[len(update) // 2])

    return answer

if __name__ == '__main__':
    from timeit import default_timer
    start_time = default_timer()
    with open('input.txt', 'r', encoding="utf-8") as file:
        data = file.read()
    print(f'\nAnswer: {solve(data)}')
    print(f'\nSeconds: {default_timer() - start_time}\n')