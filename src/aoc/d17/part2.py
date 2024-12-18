from aoc.helpers.decorators import timer


def get_combo_operand(operand, registers):
    if operand < 4:
        return operand
    elif operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]


def run_program_for_a(a, instructions):
    registers = {"A": a, "B": 0, "C": 0}
    instruction_pointer = 0
    output = ""

    while instruction_pointer < len(instructions):
        opcode = instructions[instruction_pointer]
        operand = instructions[instruction_pointer + 1]

        if opcode == 0:  # adv
            numerator = registers["A"]
            denominator = 2 ** get_combo_operand(operand, registers)
            registers["A"] = numerator // denominator
        elif opcode == 1:  # bxl
            registers["B"] = registers["B"] ^ operand
        elif opcode == 2:  # bst
            registers["B"] = get_combo_operand(operand, registers) % 8
        elif opcode == 3:  # jnz
            if registers["A"] != 0:
                instruction_pointer = operand
                continue
        elif opcode == 4:  # bxc
            registers["B"] = registers["B"] ^ registers["C"]
        elif opcode == 5:  # out
            result = get_combo_operand(operand, registers) % 8
            output += str(result) + ","
        elif opcode == 6:  # bdv
            numerator = registers["A"]
            denominator = 2 ** get_combo_operand(operand, registers)
            registers["B"] = numerator // denominator
        elif opcode == 7:  # cdv
            numerator = registers["A"]
            denominator = 2 ** get_combo_operand(operand, registers)
            registers["C"] = numerator // denominator

        instruction_pointer += 2

    return output[:-1]


def solve(puzzle_input):
    program = puzzle_input.split("\n\n")[1]
    program = program.strip().replace("Program: ", "")
    instructions = [int(instruction) for instruction in program.split(",")]

    current_options = [0]
    for i in range(len(program.replace(",", ""))):
        next_options = []
        for option in current_options:
            for int_trunc_offset in range(8):
                a = option * 8 + int_trunc_offset
                result = run_program_for_a(a, instructions)
                if result == program:
                    return a
                if program.endswith(result):
                    next_options.append(a)
        current_options = next_options

    return 0


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
