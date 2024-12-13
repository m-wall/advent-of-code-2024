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

    px += 10000000000000
    py += 10000000000000

    # x = A button presses
    # y = B button presses
    #
    # (ax * x) + (bx * y) = px
    # (ay * x) + (by * y) = py
    #
    # Eliminate x by multiplying first equation by ay and the second by ax
    # Subtract the second equation from the first equation which eliminates x
    # Rearrange and solve for y
    # Substitue y back in to solve x
    # Can be simplified to the following

    b_presses = ((px * ay) - (py * ax)) / ((bx * ay) - (by * ax))
    a_presses = (py - (by * b_presses)) / ay

    if a_presses % 1 == 0 and b_presses % 1 == 0:
        return int((a_presses * 3) + b_presses)
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