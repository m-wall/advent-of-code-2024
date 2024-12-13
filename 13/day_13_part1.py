def extract_machine_data(machine):
    config = [x.split(": ")[1] for x in machine.splitlines()]
    config = [x.split(", ") for x in config]
    ax = config[0][0].split("+")[1]
    ay = config[0][1].split("+")[1]
    bx = config[1][0].split("+")[1]
    by = config[1][1].split("+")[1]
    px = config[2][0].split("=")[1]
    py = config[2][1].split("=")[1]
    return int(ax), int(ay), int(bx), int(by), int(px), int(py)

def check_machine(machine):
    ax, ay, bx, by, px, py = extract_machine_data(machine)

    coins = list()
    for a_idx in range (1, 101):
        for b_idx in range (1, 101):
            if a_idx == 80 and b_idx == 40:
                pass

            x_total = (a_idx * ax) + (b_idx * bx)
            if x_total > px: break
            if px % x_total != 0: continue

            multiplier = int(px / x_total)

            y_total = (a_idx * ay) + (b_idx * by)
            if y_total > py: break
            if y_total * multiplier != py: continue

            coins.append((a_idx * multiplier * 3) + (b_idx * multiplier))
    if coins:
        return min(coins)
    else:
        return 0

def solve(puzzle_input):
    answer = 0
    machines = puzzle_input.split("\n\n")

    for machine in machines:
        answer+= check_machine(machine)
    
    return answer

if __name__ == '__main__':
    from timeit import default_timer
    start_time = default_timer()
    with open('input.txt', 'r', encoding="utf-8") as file:
        data = file.read()
    print(f'\nAnswer: {solve(data)}')
    print(f'\nSeconds: {default_timer() - start_time}\n')