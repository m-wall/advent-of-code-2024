def solve(puzzle_input):
    answer = 0

    if len(puzzle_input) % 2 != 0:
        puzzle_input += '0'

    pairs =[(puzzle_input[i], puzzle_input[i+1]) for i in range(0, len(puzzle_input), 2)]

    disk_map = []

    # Prepare data structure
    for id, pair in enumerate(pairs):
        file_blocks_length, space_blocks_length = pair
        disk_map.append([[(id, int(file_blocks_length))], int(space_blocks_length)])

    # Do moves
    for r_idx in range(len(disk_map) - 1, -1, -1):
        move_item = disk_map[r_idx][0][0]
        space_required = move_item[1]
        
        for f_idx, item in enumerate(disk_map):
            if f_idx >= r_idx: break
            if item[1] >= space_required:
                disk_map[f_idx][0].append(move_item)
                disk_map[f_idx][1] -= space_required
                disk_map[r_idx - 1][1] += space_required
                disk_map[r_idx][0].pop(0)
                if not disk_map[r_idx][0]:
                    disk_map[r_idx][1] == 0
                break
    
    # Calculate answer
    overall_index = 0
    for item in disk_map:
        files = item[0]
        space = item[1]
        for file in files:
            for i in range(1, file[1] + 1):
                answer += file[0] * overall_index
                overall_index += 1
        overall_index += space

    return answer

if __name__ == '__main__':
    from timeit import default_timer
    start_time = default_timer()
    with open('input.txt', 'r', encoding="utf-8") as file:
        data = file.read()
    print(f'\nAnswer: {solve(data)}')
    print(f'\nSeconds: {default_timer() - start_time}\n')