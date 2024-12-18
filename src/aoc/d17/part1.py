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


def run_program(instructions, registers):
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
    register_block, program = puzzle_input.split("\n\n")

    registers = {}
    for line in register_block.split("\n"):
        name, value = line.replace("Register ", "").split(": ")
        registers[name] = int(value)

    instructions = [int(instruction) for instruction in program.strip().replace("Program: ", "").split(",")]
    return run_program(instructions, registers)


@timer
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f"\nAnswer: {solve(data)}")


if __name__ == "__main__":
    main()
